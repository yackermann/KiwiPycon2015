import json 
from datetime import datetime as time
class Task:
    def __init__(self, id, r):
        self.r    = r
        self.id   = id
        self.data = ''

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

        else:
            return '{}'

    def getJSON(self, ip):
        if ip in self.running:
            return self.running[ip].json()
        else:
            return '{}'

    def updateStatus(self, ip):
        if ip in self.running:
            self.running[ip].setTimestamp()

    def failTask(self, ip):
        if ip in self.running:
            task = self.running[ip]
            self.new.append(task)
            del self.running[ip]

    def exportData(self):
        data = []
        filename = 'games.' + str(time.now()) + '.json'
        
        for res in self.complete:
            for game in res.getData():
                data.append(game)


        with open(filename, 'w') as w:
            w.write(json.dumps(data, indent=4, separators=(',', ': ')))

        print('Exported data to:', filename)


    def completeTask(self, ip, data):
        if ip in self.running:
            
            task = self.running[ip]
            task.addData(data)
            self.complete.append(task)
            del self.running[ip]

            if len(self.new) == 0 and len(self.running) == 0:
                self.exportData()
