from student import Student
from tutor import Tutor

class University:
    def __init__(self, tutors) -> None:
        self.tutors = tutors

    def use(self):
        for tutor in self.tutors:
            tutor.use()

if __name__ == "__main__":
    University([Tutor("David Dyer", [Student("Jenny", "Jenson", [12, 14, 12])])]).use()
