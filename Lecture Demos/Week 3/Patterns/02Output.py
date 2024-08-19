#Output Pattern
#print("<label>", "value")

class Lecturer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

david = Lecturer("David", 23)

print(david.age)
print(f"I am {david.name} and I am {david.age} years old. Sincerly, - {david.name}")