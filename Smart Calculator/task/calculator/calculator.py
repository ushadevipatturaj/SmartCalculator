from string import digits


# write your code here
def addition(num):
    _sum = 0
    for i in range(len(num)):
        _sum += int(num[i])
    print(_sum)


def determine_sign(sign):
    if len(sign) == 1:
        return sign
    else:
        if sign.count("-") % 2 == 0:
            return "+"
        else:
            return "-"


def arithmetic_function(num_list):
    result = 0
    temp_val = 1
    for i in num_list:
        if i in digits or ([k.isdigit() for k in i if k not in ("-" , "+")]):
            result += (int(i) * temp_val)
        elif "-" in i or "+" in i:
            sign = determine_sign(i)
            if sign == "-":
                temp_val = -1
            else:
                temp_val = 1
    print(result)




def _help():
    print("The program calculates the sum of numbers")


run = True
while run:
    user_input = input()
    if user_input == "/exit":
        print("Bye!")
        run = False
    elif user_input == "/help":
        _help()
    elif user_input == "":
        continue
    else:
        numbers = user_input.split()
        arithmetic_function(numbers)
