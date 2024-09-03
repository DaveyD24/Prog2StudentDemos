from student import Student

class Tutor:
    def __init__(self, full_name, students) -> None:
        self.full_name = full_name
        self.students = students

    def use(self):
        for student in self.students:
            print(f"{student.first_name} has failed?: {student.has_failed()}")