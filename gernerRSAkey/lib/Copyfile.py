__author__ = 'blfeng'

class Copyfile:
    def __init__(self,src,target):
        self.src = src
        self.target = target
    def copyfile(self):
        src = open(self.src,"r")
        target = open(self.target,"w")
        target.write(src.read())
        src.close()
        target.close()