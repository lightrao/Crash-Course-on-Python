# main.py
# import person

# print(person.weight)  # Alice
# print(person.NUMBER)  # Hello
# print(person.greet("Bob"))  # Hello, Bob!
# print(person.alice.name)  # Alice
# print(person.alice.introduce())  # Hello, Alice!

# sam = person.Person("sam")
# print(sam.name)
# print(sam.introduce())

# A Python package is a collection of modules that are organized in a hierarchical structure.
# A package can contain subpackages, modules, and resources such as data files and images.
from myutils import common
from myutils.sub1 import mod1
from myutils.sub2 import mod2

print(common.add(1, 2))
mod1.hello()
mod2.goodbye()
