# Inheritance, subclasses and complete example class
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

# Get all inheritance from class to subclass
class StudentAthlete(Student):
    
    def __init__(self, first, last, courses=None, sport=None):
        super().__init__(first, last, courses)
        self.sport = sport

courses = ["Python", "Java", "JavaScript", "AndroidStudio"]
jane = StudentAthlete("jane", "doe", courses, "hockey")
print(jane.courses)
# Check object hierarchy help(object)
#print(help(jane))
print(jane.sport)
print(isinstance(jane,StudentAthlete))
print(isinstance(jane,Student))