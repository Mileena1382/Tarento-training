#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks.")

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Woof!")

# Child class inheriting from Animal
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Meow!")

# Create instances of the child classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method on the instances
dog.speak()  # Output: Woof!
cat.speak()  # Output: Meow!


# In[ ]:




