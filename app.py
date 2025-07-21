# OOP Concepts in Python

## Class
A class is a blueprint for creating objects. An object has properties (attributes) and behavior (methods).

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f'{self.name} says woof!'
```

## Object
An object is an instance of a class.

```python
my_dog = Dog('Buddy', 5)
print(my_dog.bark())  # Output: Buddy says woof!'
```

## Inheritance
Inheritance allows a class to inherit attributes and methods from another class.

```python
class Puppy(Dog):
    def wean(self):
        return f'{self.name} is now weaned!'
```

## Polymorphism
Polymorphism allows methods to do different things based on the object.

```python
class Cat:
    def speak(self):
        return 'Meow'

animals = [Dog('Rex', 3), Cat()]
for animal in animals:
    print(animal.speak())  # Calls speak() for each animal
```

## Encapsulation
Encapsulation restricts access to certain attributes and methods to protect the integrity of the object's state.

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```