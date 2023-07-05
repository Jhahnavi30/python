# users - signup, login, profile, logout, users_list
# inventory - restock, display
# cart - add, clear, remove
# oder - place, checkout

#module, package(_init_.py), lib
#frameworks: [typer]
#ORM - RDBMS
#RDBMS (SQL) ==> ORM - [object relational mapper]
#sqlite
#JSON - Javascript object notation == dict
#file handling - to read write or append to file

#OOPS

#class:blueprint for creating objects with
#similar properties and methods

#classes and objects
#Inheritence, composition,mul-inheritence ,mixin


# git status
# git add filename
# git status
# git commit -m "changes made"
#git push (opens a browser, setpassword )

#classes & objects
#class has atributes,methods(class function) - class methods,static method

#class classA
#a= 10

# instance method
# def func_name(self, b, c, d):
#     b=self.a
#     print()
#     return a

# @classmethod  # class method decorator
# def func_name(cls, b, c, d):
#     b = cls.a
#     print()
#     return a

# @staticmethod #static method decorator
# def func_b(b, c, d):
#     b = cls.a
#     print()
#     return a

# methods of class
# 1. instance method = has acess to all attributes and methods
# 2. class method = can only acess class attributes and other class methods
# 3. static method = doesnt have acess to class attributes or other class/instance methods

class Student:
   def __init__(self, name, age, gender):
     self.name = name
     self.age = age
     self.gender = gender
        
   def info(self):
     print(f"name: {self.name} | age: {self.age} | gender: {self.gender}")

ram = Student("ram",18, "male")
ram.info()

class student:
    srn = 0
    name = "nickname"
    stu_class = "noclass"
    elective = []

    def init(self,name,srn,stu_class):
     self.srn = srn
     self.name = name
     self.stu_class = stu_class

    def add_elective(self,subject):
     self.elective.append(subject)

    s = student = student( "ram", 123, "2.1")
    print(student.srn)
    print(student.name)
    print(student.stu_class)

class student:
    college_name = "Reva University"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def info(self):
        marks = [1, 2, 3, 4, 5]
        self.college()
        print(f"Name: {self.name} | Age: {self.age} | Gender: {self.gender}")
        self.total_marks(marks)

    @classmethod
    def college(cls):
        print(f"College: {cls.college_name}")

    @staticmethod
    def total_marks(marks_list):
        total = 0
        for mark in marks_list:
            total = total + mark
        print(f"Total marks = {total}")
        return total


# Create an instance of the student class
student1 = student("John", 20, "Male")

# Call the info method to display student information
student1.info()