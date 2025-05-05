class Student:
    def __init__(self, name, age, grade):
        self.name  = name
        self. age = age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
      # self.is_active = False --i can add any fun to my def method even i didn't write it before

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade() # here i can write .grade but it's not accurate bcoz it's better wo write
                                         # the def method name that i know for sure that it will not change
        return value / len(self.students)

s1 = Student('Oday', 33, 79)
s2 = Student('Ghena', 27, 85)
s3 = Student('Leia', 12, 63)

course = Course('Math', 2)
course.add_student(s2)
course.add_student(s3)
print(course.add_student(s3)) # bcoz the max_student is only 2 and that's why it will not effect our average grade
# print(course.students[0].name) to run the first element of my adding list
print(course.get_average_grade())