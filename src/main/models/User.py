import json

class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def getName(self):
        return self.name