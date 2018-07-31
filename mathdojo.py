class python:
    def __init__(self, total=0):
        self.total=total
    def adding(self, number, *args):
        self.total+=number
        for i in args:
            self.total+=i
        return self
    def subtracting(self, number, *args):
        self.total-=number
        for i in args:
            self.total-=i
        return self
    def result(self):
        print(self.total)
md=python()

md.adding(2).adding(2,5,1).subtracting(3,2).result()

