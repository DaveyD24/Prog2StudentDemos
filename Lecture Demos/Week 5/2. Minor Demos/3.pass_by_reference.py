def double_me(x) -> int:
    x = x * 2
    return x

def add_an_item_to_me(x) -> list:
    x.append(5)
    return x

if __name__ == "__main__":
    my_int = 4
    my_list = [1,2,3,4]

    print(f"Value After doubling: {double_me(my_int)}")
    print(f"Value of my original variable: {my_int}")

    print(f"Value after appending: {add_an_item_to_me(my_list)}")
    print(f"Value of original list: {my_list}")