from Model.Premiership import Premiership

adder = lambda x, y : x + y
def multiply(n):
    return lambda x: x * n

# print(myadder(2, 7))

doubler = multiply(2)
tripler = multiply(3)

# print(mydoubler(8))
# print(mytripler(8))

x = 4
def square_that_int(n):
    return n * n
# print(square_that_int(x))

name = "David"
def print_that_string(s):
    print(s)
# print_that_string(name)

teams = ['Titans', 'Storm', 'Roosters', 'Broncos']
mappedTeams = map(lambda team : team.upper(), teams)
# print(list(mappedTeams))

premiership = Premiership()
premiership.play_season()
print(premiership.premiers())