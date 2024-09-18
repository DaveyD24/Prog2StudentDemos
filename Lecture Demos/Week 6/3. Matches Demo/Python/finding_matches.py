#A more advanced method using list comprehension
#return [result for item in collection if condition]
def zWords2(words):
    return [word.upper() for word in words if 'z' in word]

def is_z_word(word):
    return 'z' in word

def zWords(words):
    matches = []
    for word in words:
        if is_z_word(word):
            matches.append(word)
    return matches

words = ["snooze", "david", "zed", "dyer"]
print(f"Matching words: \n{zWords(words)}")