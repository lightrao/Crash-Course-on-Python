# main.py
import person

print(person.weight)  # Alice
print(person.NUMBER)  # Hello
print(person.greet("Bob"))  # Hello, Bob!
print(person.alice.name)  # Alice
print(person.alice.introduce())  # Hello, Alice!

sam = person.Person("sam")
print(sam.name)
print(sam.introduce())
