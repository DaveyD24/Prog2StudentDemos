class Student:
    def __init__(self, first_name, last_name, marks):
        self.first_name = first_name
        self.last_name = last_name
        self.marks = marks
    
    #encapsulation
    #information related to the field is exported to the user; but not the field itself
    def get_grade(self) -> int:
        total = 0
        for mark in self.marks:
            total += mark
        if total < 50:
            return "F"
        return "P"


if __name__ == "__main__":
    david = Student("David", "Dyer", [12, 20, 9])
    print(f"Davids grade for Prog2: {david.get_grade()}")