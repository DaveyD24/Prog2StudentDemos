class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence

    def display(self):
        print("--------------------------------")
        print(f"{sentence}:")
        print(f"Total words in sentence: {self.word_count()}")
        print(f"Number of z words in sentence: {self.z_count()}")
        print(f"Sentence is pascal case" if self.is_pascal_case() else "Sentence is not pascal case")
        print("--------------------------------")

    def word_count(self):
        return len(self.sentence.split(" "))

    def z_count(self):
        count = 0
        for word in self.sentence.split(" "):
            if self.contains_z(word):
                count = count + 1
        return count

    def contains_z(self, word):
        return "z" in word.lower()

    #Advanced feature
    def is_pascal_case(self):
        for word in self.sentence.split(" "):
            if word[0].islower():
                return False
        return True

if __name__ == "__main__":
    sentences = ["David is zhe worst tutor ever", "The Big Brown Fox Did Some Stuff I Guess", "time to muzz", "Example sentence", "exampleZ SentenzeZ"]
    for sentence in sentences:
        Sentence(sentence).display()