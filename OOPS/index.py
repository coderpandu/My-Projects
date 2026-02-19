# class Student:
#     name = "Sumit"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

# class Student:

#     college_name = "MIT"

#     def __init__(self, fullname, lastname, marks):
#         self.name = fullname
#         self.surname = lastname
#         self.marks = marks
#         print("Adding new student in Database")

#     def hello(self):
#         print("Hello, " + self.name + " " + self.surname)

#     def get_marks(self):
#         return self.marks

# s1 = Student("sumit", "phuyal", 90)
# print(s1.name + " " + s1.surname + "," + s1.college_name + "," + str(s1.marks))

# s2 = Student("Ram", "Sharma", 80)
# print(s2.name + " " + s2.surname + "," + s2.college_name + "," + str(s2.marks))

# s3 = Student("Hari", "Kumar", 70)
# print(s3.name + " " + s3.surname + "," + s3.college_name + "," + str(s3.marks))

# s1.hello()
# s2.hello()
# s3.hello()


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_marks(self):
#         sum = 0
#         for mark in self.marks:
#             sum += mark
#         print("Hi", self.name, "your average marks are: ", sum / len(self.marks))

# s1 = Student("Sumit Phuyal", [80, 70, 92])
# s1.get_marks()


# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brake = False
#         self.clutch = False

#     def start_engine(self):
#         self.clutch = True
#         self.acc = True
#         print("Engine started")

# car1 = Car()
# car1.start_engine()



