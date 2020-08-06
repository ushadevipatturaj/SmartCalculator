# write your code here
def addition(num):
    _sum = 0
    for i in range(len(num)):
        _sum += int(num[i])
    print(_sum)


def help():
    print("The program calculates the sum of numbers")


run = True
while run:
    user_input = input()
    if user_input == "/exit":
        print("Bye!")
        run = False
    elif user_input == "/help":
        help()
    elif user_input == "":
        continue
    else:
        numbers = user_input.split()
        addition(numbers)