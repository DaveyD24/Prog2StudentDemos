names = []

def anyEmptyNames():
    for name in names:
        if name == "":
            return True
    return False

name = ""
while (name := input("Name: ")) != "X":
    names.append(name)
if anyEmptyNames():
    print("Invalid Data!")
