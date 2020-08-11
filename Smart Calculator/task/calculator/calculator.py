from string import digits, ascii_letters


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
        if i in ascii_letters or (len(i) > 1 and (any([k in ascii_letters for k in i if k not in ("-", "+")]))):
            print("Invalid expression")
            return 0
        if i in digits or ([k.isdigit() for k in i if k not in ("-", "+")]):
            if len(num_list) == 1 and (i.endswith("+") or i.endswith("-")):
                print("Invalid expression")
                return 0
            else:
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
    elif "/" in user_input and user_input not in ("/exit", "/help"):
        print("Unknown command")
    else:
        numbers = user_input.split()
        arithmetic_function(numbers)
