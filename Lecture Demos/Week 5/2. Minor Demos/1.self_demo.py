class Lecturer:
    def __init__(self, name, subject, student_marks) -> None:
        self.name = name
        self.subject = subject
        self.student_marks = student_marks
      
    def get_mark(self, index_of_student):
        return self.student_marks[index_of_student]
    
    def increase_mark(self, index_of_student, amount):
        self.student_marks[index_of_student] += amount

if __name__ == "__main__":
    david = Lecturer("David", "Programming 2", [48, 12, 98, 96, 51])
    print(f"First students mark before adjustment: {david.get_mark(0)}")
    david.increase_mark(0, 10)
    print(f"First students mark after adjustment: {david.get_mark(0)}")


#Due to the way python is designed, you can think of the increase_mark function as existing on its own
#It has to be directly told what object you're referring to
#Python does this for you, by converting this:
#   david.increase_mark(0, 10)
#to this:
#   David.increase_mark(david, 0, 10)
#The weird thing is, the function will not RECEIVE the object on its own
#You have to explicitly write your function to expect to receive that object as its first parameter, like so:
#   def increase_mark(object, index_of_student, amount)
#However, we ALWAYS name that parameter self to follow convention