from student import Student

class University:
    def __init__(self) -> None:
        pass

    def use(self):
        david = Student("David", "Dyer", [12, 20, 11])
        print(f"Davids grade for Prog2: {david.grade()}")
        print(f"Has David failed an assignment?: {david.has_failed_assessment()}")

if __name__ == "__main__":
    University().use()