# main.py
# -----------------------------------------------------------------------------------------------
# module: python file containing function and variable that can be imported and used in other file
import greet

greet.hello("Neo")
print(greet.age)

# The dir() function in Python returns a list of names defined by an object.
# If the object is a module, it returns the names of the variables, functions, classes, etc. defined in the module.
# If the object is a class or an instance of a class, it returns the names of the attributes and methods of the class or instance.
print(dir(greet))

# The dir() function with no parameter returns the list of names in the current local scope.
# This includes the names of the variables, functions, modules, etc. that are defined or imported
# in the current scope.
print(dir())

# -----------------------------------------------------------------------------------------------
# import the modules directly
from mypackage import hello, goodbye

# use the functions from the modules
hello.say_hello("Charlie")
goodbye.say_goodbye("David")

# -----------------------------------------------------------------------------------------------
# import the common module directly
import myutils.common

print(myutils.common.add(1, 2))
print(myutils.common.sub(1, 2))
print(myutils.common.mul(1, 2))
print(myutils.common.div(1, 2))
