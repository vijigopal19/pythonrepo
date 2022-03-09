class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def myval(self):
        print("hello.. my value is ", self.x)


p1 = MyClass(20, 30)
p1.myval()
print("X's value is : ", p1.x)
print("Y's value is : ", p1.y)
