# write the function to calculate 2nd power of a number
# return the result from the function and print the result

base = 3
exponent = 4

result = 1

for exponent in range(exponent, 0, -1):
    result *= base

print("Answer = " + str(result))


def power_2(a: int):
    return a ** 2

print(power_2(6))

# write a function to calculate a**n
def exponentiate(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result
base = 2
power = 5
result = exponentiate(base, power)
print(result)


#Python function that returns a dictionary
def myAnimals(a1,a2,a3):
    Animalgroup = {'Kitten':a1,'Puppy':a2,'Pup':a3}
    return Animalgroup

output = myAnimals("Cat","Dog","Rat")
print(output)

#classes
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

