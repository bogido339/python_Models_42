class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def me(slef):
    print("hello")

class Student(Person):
  def __init__(self, name, age, levle):
    Person.__init__(name, age)
    self.levle = levle


p = Person("mohamed", 20)
s = Student("yassin", 22, 2.92)

print(p.name, p.age)
print(s.name, s.age, s.levle)
p.me()
s.me()

