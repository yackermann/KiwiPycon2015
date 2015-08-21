import json 
from datetime import datetime as time
class Task:
    def __init__(self, id, r):
        self.r  = r
        self.id = id

    def addData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setTimestamp(self):
        self.timestamp = time.now()

    def getTimestamp(self):
        return self.timestamp

    def json(self):
        return json.dumps({
            'start' : self.r.start,
            'stop'  : self.r.stop,
            'step'  : self.r.step
        })

class TaskList:
    def __init__(self):
        self.new = []
        self.complete = []
        self.running = {}

    def addTask(self, id, r):
        self.new.append(Task(id, r))

    def getTask(self, ip):
        if len(self.new) > 0 and ip not in self.running:
            task = self.new.pop()
            task.setTimestamp()
            self.running[ip] = task
            return task.json()
        elif ip in self.running:
            return self.running[ip].json()

    def getJSON(self, ip):
        if ip in self.running:
            return self.running[ip].json()

    def updateStatus(self, ip):
        if ip in self.running:
            self.running[ip].setTimestamp()

    def failTask(self, ip):
        if ip in self.running:
            task = self.running[ip]
            del self.running[ip]
            self.new.append(task)

    def completeTask(self, ip, data):
        if ip in self.running:
            task = self.running[ip]
            task.addData(data)
            del self.running[ip]
            self.complete.append(task)