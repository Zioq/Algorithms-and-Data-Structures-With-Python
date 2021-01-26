#  Special methods and what they are

# Diffrence between __str__ & __repr__
""" str() is used for creating output for end user while repr() is mainly used for debugging and development. repr’s goal is to be unambiguous and str’s is to be readable. 

if __repr__ is defined, and __str__ is not, the object will behave as though __str__=__repr__.

This means, in simple terms: almost every object you implement should have a functional __repr__ that’s usable for understanding the object. Implementing __str__ is optional
"""

class Student:

    def __init__(self, first, last, courses=None ):
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses
    
    def add_course(self, new_course):
        if new_course not in self.courses:
            self.courses.append(new_course)
        else:
            print(f"{self.first_name} is already enrolled in the {new_course} course")
        
    def remove_course(self, remove_course):
        if remove_course in self.courses:
            self.courses.remove(remove_course)
        else:
            print(f"{remove_course} not found")

    def __len__(self):
        return len(self.courses)

    def __repr__(self):
        return f"Sturdent('{self.first_name}', '{self.last_name}', '{self.courses}')"

    def __str__(self):
        return f"First name: {self.first_name.capitalize()}\nLast name: {self.last_name.capitalize()}\nCourses: {', '.join(map(str.capitalize, self.courses))}"



courses_1 = ['python', 'go', 'javascript']
courses_2 = ['java', 'go', 'c']
# Create new object of class
robert = Student("Robert", "Han")
john = Student("John", "Smith",courses_2)

print(robert.first_name, robert.last_name, robert.courses)
print(john.first_name, john.last_name, john.courses)

# Add new course using a method
john.add_course("java")
robert.add_course("PHP")
print(robert.first_name, robert.last_name, robert.courses)

# Remove course using a method
john.remove_course("c")
john.remove_course("c")
john.remove_course("python")
print(john.first_name, john.last_name, john.courses)

# use __str__ method
print(robert)
print(john)

# use __dict__ method
print(robert.__dict__)

# use repre method
print(repr(robert))
print(repr(john))


# use len functionality
print(len(robert)) # return how many courses robert enrolled.
