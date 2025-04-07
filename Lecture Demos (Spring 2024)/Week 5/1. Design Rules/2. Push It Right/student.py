class Student:
    def __init__(self, first_name, last_name, marks):
        self.first_name = first_name
        self.last_name = last_name
        self.marks = marks
    
    def grade(self) -> str:
        total = 0
        for mark in self.marks:
            total += mark
        if total >=50:
            return "P"
        return "F"
    
    #for University to calculate this, it would need access to the internals of Student
    #instead, Student provides only the information University needs
    def has_failed_assessment(self):
        for mark in self.marks:
            if mark < 10:
                return True
        return False