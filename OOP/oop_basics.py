"""
oop_basics.py
--------------
This file demonstrates core OOP concepts:
- Class
- Object
- Attributes
- Methods
- Updating object data
"""

class Student:
    """
    A class to represent a student.
    """

    def __init__(self, name, student_id, major):
        # Attributes
        self.name = name
        self.student_id = student_id
        self.major = major
        self.is_active = True

    def display_info(self):
        """
        Display student information.
        """
        print("Student Information")
        print("-------------------")
        print(f"Name       : {self.name}")
        print(f"ID         : {self.student_id}")
        print(f"Major      : {self.major}")
        print(f"Active     : {self.is_active}")

    def change_major(self, new_major):
        """
        Change the student's major.
        """
        self.major = new_major
        print(f"Major updated to: {self.major}")

    def deactivate(self):
        """
        Deactivate the student.
        """
        self.is_active = False
        print(f"{self.name} is now inactive.")


def main():
    # Create a student object
    student1 = Student("Md Rasel", "CSE2023", "Computer Science")

    # Display initial information
    student1.display_info()
    print()

    # Change major
    student1.change_major("Software Engineering")
    print()

    # Deactivate student
    student1.deactivate()
    print()

    # Display updated information
    student1.display_info()


if __name__ == "__main__":
    main()
