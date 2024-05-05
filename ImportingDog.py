from Dog import *

# Creating an instance of Dog
my_dog = Dog(breed="Labrador Retriever", age=3, color="Golden")
# Accessing attributes and calling methods
print(f"My dog is a {my_dog.color} {my_dog.breed} and is {my_dog.age} years old.")
my_dog.bark()
my_dog.sleep()
my_dog.eat()