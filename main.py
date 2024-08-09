class Parent:
  def method(self):
    print("pa")

class A(Parent):
  def method(self):
    print("a")

class B(Parent):
  def method(self):
    print("b")



flag = False


if flag:
  b = A()
  b.method()

else:
  b = B()
  b.method()
