from http.server import BaseHTTPRequestHandler, HTTPServer
from tasklist import *
import re, cgi

man = TaskList()
x = ''
post = ''
class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','application/json')
        self.end_headers()
        
        ip = self.client_address[0]

        if(self.path == '/get'):
            print('Getting task for:', ip)
            self.wfile.write(man.getTask(ip).encode('utf-8'))
        else:
            self.wfile.write('{}'.encode('utf-8'))

    def do_POST(self):
        self.send_response(200)
        self.send_header('content-type','application/json')
        self.end_headers()

        ip = self.client_address[0]

        if self.path == '/post':

            form = cgi.FieldStorage(
                fp=self.rfile, 
                headers=self.headers,
                environ={'REQUEST_METHOD':'POST',
                        'CONTENT_TYPE':self.headers['Content-Type'],
                        })

            if 'method' in form:
                method = form['method'].value
                if method == 'update':
                    man.updateStatus(ip)
                    print('Success update')

                elif method == 'data':
                    if 'data' in form:
                        data = form['data'].value
                        try:
                            d = json.loads(data)
                            man.completeTask(ip, d)
                            print('Success data')
                        except Exception as e:
                            print(e)
                            man.failTask(ip)
                            print('Failed data')
                    else:
                        print('No data')

                else:
                     self.wfile.write('{}'.encode('utf-8'))




        else:
            self.wfile.write('{}'.encode('utf-8'))

    def log_message(self, format, *args):
        return


was = 0
step = 10
for i in range(2500, 1000000, 2500):
    id = str(was) + '-' + str(i)
    man.addTask(id, range(was, i, step))
    was = i

print('Starting server...')

serv = HTTPServer( ( '0.0.0.0' , 8888 ) , HttpProcessor )
serv.serve_forever()