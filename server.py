from http.server import BaseHTTPRequestHandler, HTTPServer
from tasklist import *
import cgi
manager = TaskList()

manager.addTask('test', range(0, 100, 10))

class HTTPProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','application/json')
        self.end_headers()

        ip = self.client_address[0]

        task = manager.getTask(ip)
        self.wfile.write(task.encode('utf-8'))
    
        print('Getting get request from', self.client_address)

    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type','application/json')
        self.end_headers()

        ip = self.client_address[0]

        form = cgi.FieldStorage(
            fp      = self.rfile, 
            headers = self.headers,
            environ = {
                'REQUEST_METHOD' : 'POST',
                'CONTENT_TYPE'   : self.headers['Content-Type'],
            }
        )

        if 'method' in form:
            if form['method'].value == 'data':
                if 'data' in form:
                    rawData = form['data'].value
                    try:
                        data = json.loads(rawData)
                        manager.completeTask(ip, data)
                        print('Success data')
                    except Exception as e:
                        print(e)
                        manager.failTask(ip)
                        print('Failed data')
                else:
                    print('No data')  

        print('Getting post request from', ip, form)



address = ( '0.0.0.0', 8888 )

server = HTTPServer(address, HTTPProcessor)
print('Staring server at', address[0], 'port', address[1])
server.serve_forever()