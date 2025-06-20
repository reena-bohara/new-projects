class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hey, my name is {self.name} and I am {self.age} years old.")

# create an object from a person class
student1 = person("riya", 25)
student2 = person("seema",28)
student3 = person("sapna",26)

# Access the object's attributes
print(student1.name)
print(student1.age) 
print(student2.name) 
print(student2.age) 
print(student3.name) 
print(student3.age) 

# call the object's method
student1.greet()
student2.greet()
student3.greet()