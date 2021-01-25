
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