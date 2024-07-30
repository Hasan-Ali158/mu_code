class employee:

    def putdata(self):
        self.id=int(input("Enter employee id:"))
        self.name=input("Enter employee name:")
        self.salery=int(input("Enter employee salery:"))

    def dsiplay(self):
        print("employee id:",self.id)
        print("employee name:",self.name)
        print("employee salery:",self.salery)

a=employee()
a.putdata()
a.dsiplay()
b=employee()
b.putdata()
b.dsiplay()
