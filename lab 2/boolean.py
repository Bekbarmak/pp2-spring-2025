# Boolean Values
print(12 > 9)
print(10 == 9)
print(2 < 6)

a = 200
b = 201
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

# Most Values are True
print(bool("abc"))
print(bool(123))
print(bool(["apple", "banana", "strawberry"]))

# Some Values are False
print(bool(False))
print(bool(0))
print(bool([]))
print(bool(None))
print(bool(""))
print(bool(()))
print(bool({}))

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

# Functions can Return a Boolean
def myFunction():
    return True

print(myFunction())
if myFunction():
    print("YES!")
else:
    print("NO!")

x = 200
print(isinstance(x,int))

# EXERCISES
print(5 > 3)
# True

print(10 > 9)
# True

print(10 == 9)
# False

print(10 < 9)
# False

print(bool("abc"))
# True

print(bool(0))
# False