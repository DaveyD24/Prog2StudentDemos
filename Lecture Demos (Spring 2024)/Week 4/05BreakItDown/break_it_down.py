#Show the number of words that contain a lowercase vowel
def isVowel(c):
    return c in "aeiou"


def containsVowel(word):
    for c in word:
        if isVowel(c):
            return True
    return False

def matches(sentence):
    count = 0
    for word in sentence.split():
        if containsVowel(word):
            count = count + 1
    return count

sentence = input("Sentence: ")
print(f"The number of words with a vowel is {matches(sentence)}")












# def isVowel(letter: chr):
#     if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
#         #show improved version in lecture
#         return True
#     return False

# def anyVowels(word: str):
#     for c in word:
#         if isVowel(c):
#             return True
#     return False


# def matchingWords(sentence: str):
#     count = 0
#     for word in sentence.split():
#         if anyVowels(word):
#             count = count + 1
#     return count

# sentence = input("Sentence: ")
# print(f"Matching words: {matchingWords(sentence)}")
