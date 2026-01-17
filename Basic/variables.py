"""
variables.py
-------------
This file demonstrates:
- Variables
- Common data types
- Basic operations in Python
"""

def main():
    # Integer variable
    age = 23

    # Float variable
    height = 5.6

    # String variable
    name = "Md Rasel"

    # Boolean variable
    is_student = True

    # Print variables and their types
    print("Name:", name, "| Type:", type(name))
    print("Age:", age, "| Type:", type(age))
    print("Height:", height, "| Type:", type(height))
    print("Is Student:", is_student, "| Type:", type(is_student))

    print("\n--- Basic Operations ---")

    # Arithmetic operations
    year_of_birth = 2026 - age
    print("Estimated year of birth:", year_of_birth)

    # String concatenation
    full_intro = "My name is " + name + " and I am learning Python."
    print(full_intro)

    # Boolean logic
    print("Am I a student?", is_student)


if __name__ == "__main__":
    main()
