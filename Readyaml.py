import yaml
from Test.Test import Test

class Readyaml:
    def __init__(self):
        self.fileName = 'python-rest-api-using-flask/Test/dependency.yaml'

    def checkDependency(self, processName):
        with open(self.fileName, 'r') as file:
            depedencies = yaml.safe_load(file)
            x = depedencies['pipeline'][processName]
            for i in x:
                print(i)


Test = Readyaml()
Test.checkDependency('TOPSTOCK')
