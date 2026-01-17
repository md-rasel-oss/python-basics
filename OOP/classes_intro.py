"""
classes_intro.py
-----------------
This file introduces:
- Classes
- Objects
- Attributes
- Methods
"""

class Person:
    """
    A simple class to represent a person.
    """

    def __init__(self, name, age, country):
        # Attributes (data)
        self.name = name
        self.age = age
        self.country = country

    def introduce(self):
        """
        Method to introduce the person.
        """
        print(f"Hi, my name is {self.name}.")
        print(f"I am {self.age} years old.")
        print(f"I am from {self.country}.")


def main():
    # Creating objects (instances of the class)
    person1 = Person("Md Rasel", 23, "Bangladesh")
    person2 = Person("Alex", 25, "China")

    # Calling methods on objects
    person1.introduce()
    print("-" * 30)
    person2.introduce()


if __name__ == "__main__":
    main()
