"""TaskList class
Yuriy Ackermann, 2015 
ackermann.yuriy@gmail.com
The MIT License (MIT)
"""

import json 
from datetime import datetime as time
class Task:
    """Task Class"""
    def __init__(self, id, r):
        self.r    = r
        self.id   = id
        self.data = ''

    def addData(self, data):
        """Assets Task data value"""
        self.data = data
        self.cache()

    def cache(self):
        """Caches Task data"""
        with open('cache/' + str(self.id) + '.json', 'w') as cache:
            cache.write(json.dumps(self.data, indent=4, separators=(',', ': ')))

    def getData(self):
        """Returns Tasks data"""
        return self.data

    def setTimestamp(self):
        """Sets Task timestamp"""
        self.timestamp = time.now()

    def getTimestamp(self):
        """Returns Task timestamp"""
        return self.timestamp

    def json(self):
        """Returns JSON value encoded Task"""
        return json.dumps({
            'start' : self.r.start,
            'stop'  : self.r.stop,
            'step'  : self.r.step
        })

class TaskList:
    """TaskList Class"""
    def __init__(self):
        self.new = []
        self.complete = []
        self.running = {}

    def addTask(self, id, r):
        """Adds new Task to TaskList"""
        self.new.append(Task(id, r))

    def getTask(self, ip):
        """Returns Task from TaskList, specified by ip address"""
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
        """Return JSON encoded Task, specified by ip address"""
        if ip in self.running:
            return self.running[ip].json()
        else:
            return '{}'

    def updateStatus(self, ip):
        """Updates Task timestamp, specified by ip address"""
        if ip in self.running:
            self.running[ip].setTimestamp()

    def failTask(self, ip):
        """Fails Task, specified by ip address"""
        if ip in self.running:
            task = self.running[ip]
            lastTask = self.new.pop()
            self.new.append(task)
            self.new.append(lastTask)
            del self.running[ip]

    def exportData(self):
        """Exports all data to JSON file"""
        data = []
        filename = 'games.' + str(time.now()) + '.json'
        
        for res in self.complete:
            for game in res.getData():
                data.append(game)


        with open(filename, 'w') as w:
            w.write(json.dumps(data, indent=4, separators=(',', ': ')))

        print('Exported data to:', filename)


    def completeTask(self, ip, data):
        """Completes task specified by ip address"""
        if ip in self.running:
            
            task = self.running[ip]
            task.addData(data)
            self.complete.append(task)
            del self.running[ip]

            if len(self.new) == 0 and len(self.running) == 0:
                self.exportData()
