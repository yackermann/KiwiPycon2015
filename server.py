from http.server import BaseHTTPRequestHandler, HTTPServer
from tasklist import *
import cgi, time
manager = TaskList()

timestamp = 0.0
complete = False

class HTTPProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        global timestamp, complete
        self.send_response(200)
        self.send_header('content-type','application/json')
        self.end_headers()

        ip = self.client_address[0]

        if not timestamp:
            timestamp = time.perf_counter()

        if len(manager.new) or len(manager.running):
            if self.path == '/':
                print('\033c')
                print('Tasks running:',  len(manager.running))
                print('Tasks complete:', len(manager.complete))
                print('Tasks left:',     len(manager.new))

                print('Getting task for', self.client_address[0])
        else:
            if not complete:
                print('\033c')
                print('Time taken', time.perf_counter() - timestamp)
                print('Total tasks', len(manager.complete))
                complete = True

        task = manager.getTask(ip)
        self.wfile.write(task.encode('utf-8'))
        
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
                        print('Succeed data', ip)
                    except Exception as e:
                        print(e)
                        manager.failTask(ip)
                        print('Failed data', ip)
                else:
                    print('No data', ip)  

    def log_message(self, format, *args):
        return

def generateTasks():
    was = 0
    step = 10
    for i in range(2500, 1000000, 2500):
        id = str(was) + '-' + str(i)
        manager.addTask(id, range(was, i, step))
        was = i

generateTasks()

address = ( '0.0.0.0', 8888 )

server = HTTPServer(address, HTTPProcessor)
print('Staring server at', address[0], 'port', address[1])
server.serve_forever()