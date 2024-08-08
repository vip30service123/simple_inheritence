class Parent:
  def method(self):
    print("pa")

class A(Parent):
  def method(self):
    print("a")

class B(Parent):
  def method(self):
    print("b")



b = B()
b.method()