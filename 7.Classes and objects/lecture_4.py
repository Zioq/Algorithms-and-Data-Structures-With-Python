# Reading from and writing to files

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

    def find_in_file(self,filename):
        with open(filename) as f:
            for line in f:
                first_name, last_name, course_details = Student.prep_record(line.strip())
                # create Student object
                student_read_in = Student(first_name, last_name, course_details)
                if self == student_read_in:
                    return True
            return False 
            

    def add_to_file(self,filename):
        if self.find_in_file(filename):
            return "Record already exists"
        else:
            record_to_add = Student.prep_to_write(self.first_name, self.last_name, self.courses)
            # Add new student data in txt file
            with open(file_name, "a+") as to_write:
                to_write.write(record_to_add+"\n")
            return "Record Added"


    @staticmethod #Assign as static method in Class
    def prep_record(line):
        line = line.split(":")
        first_name, last_name = line[0].split(",")
        course_details = line[1].rstrip().split(",")
        return first_name, last_name, course_details

    @staticmethod
    def prep_to_write(first_name, last_name, courses):
        full_name = first_name +','+ last_name
        courses = ",".join(courses)
        return full_name+":"+courses
    
    # method to comparing objects
    def __eq__(self,other):
        return self.first_name == other.first_name \
        and self.last_name == other.last_name

    def __len__(self):
        return len(self.courses)

    def __repr__(self):
        return f"Sturdent('{self.first_name}', '{self.last_name}', '{self.courses}')"

    def __str__(self):
        return f"First name: {self.first_name.capitalize()}\nLast name: {self.last_name.capitalize()}\nCourses: {', '.join(map(str.capitalize, self.courses))}"

file_name = "data.txt"
robert = Student("robert","han",["python","ruby","javascript"])
print(robert.find_in_file(file_name))
print(robert.add_to_file(file_name))
joe = Student("john", "snow", ["python","ruby","java"])
print(joe.find_in_file(file_name))
print(joe.add_to_file(file_name))