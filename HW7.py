class InvalidAgeError(Exception):
    def __init__(self, message):
        super().__init__(message)
class Person:
    def __init__(self, name):
        self.name = name
        self.age = None
    def setage(self, age):
        if age < 0 or age > 120:
            raise InvalidAgeError("Your age must be from 0 to 100")
        self.age = age
try:
    person = Person("Daniil")
    person.setage(130)
except InvalidAgeError as e:
    print(f"Error: {e}")
try:
    person.setage(-10)
except InvalidAgeError as e:
    print(f"Error: {e}")
try:
    person.setage(25)
    print(f"Age {person.name}: {person.age}")
except InvalidAgeError as e:
    print(f"Error: {e}")






class MyIterator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return iter(range(self.n + 1))

    def count_down(self):
        return (i for i in range(self.n, -1, -1))

    def multiplier(self, m):
        return lambda x: x * m


def print_result(func):
    def wrapper(args, wargs):
        result = func(args, wargs)
        print(f"Result: {result}")
        return result
    return wrapper
print("Iterator:")
for num in MyIterator(5):
    print(num)
print("Generator:")
for num in MyIterator(5).count_down():
    print(num)

def add(a, b):
    return a + b


print("Decorator:")
add(3, 4)

print("Closure:")
times_three = MyIterator(5).multiplier(3)
print(times_three(10))