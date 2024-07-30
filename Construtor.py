class faculty:

    def __init__(self,a,b,c):    #constructor
        self.id=a
        self.name=b
        self.salery=c

    def display(self):
        print(self.id)
        print(self.name)
        print(self.salery)

a=faculty(1,"Hasan",20000)
a.display()
b=faculty(2,"Ali",20000)
b.display()
