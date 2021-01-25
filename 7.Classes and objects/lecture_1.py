# Build Student class
# Make a first word of class name as capitalize letter

class Student:

    # `self` means a instance of class itself 
    # To allow the no course case and fix the error, assign `None` to a relevent parameter
    def __init__(self, first, last, courses=None ):
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses
        

    pass


courses_1 = ['python', 'go', 'javascript']
courses_2 = ['java', 'go', 'c']
# Create new object of class
robert = Student("Robert", "Han")
john = Student("John", "Smith",courses_2)


print(robert.first_name, robert.last_name, robert.courses)
print(john.first_name, john.last_name, john.courses)
