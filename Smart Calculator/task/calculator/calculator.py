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
    global variable_dict
    num_list_temp = []
    result = 0
    temp_val = 1
    for i in num_list:
        if i in ("+", "-") or i.isnumeric():
            num_list_temp.append(i)
        elif i.isalpha() and i in variable_dict:
            num_list_temp.append(variable_dict[i])
        elif i.isalpha() and i not in variable_dict:
            print("Unknown variable")
        elif "-" in i or "+" in i:
            num_list_temp.append(determine_sign(i))

    for i in num_list_temp:
        if i in ascii_letters or (len(i) > 1 and (any([k in ascii_letters for k in i if k not in ("-", "+")]))):
            print("Invalid expression")
            return 0
        if i in digits or ([k.isdigit() for k in i if k not in ("-", "+")]):
            if len(num_list_temp) == 1 and (i.endswith("+") or i.endswith("-")):
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



def variable_store(var_list):
    global variable_dict
    if var_list[0].isalpha() and not any(char.isdigit() for char in var_list[0]):
        if var_list[1].isalpha() and var_list[1] in variable_dict:
            variable_dict[var_list[0]] = variable_dict[var_list[1]]
        elif var_list[1].isalpha() and var_list[1] not in variable_dict:
            print("Unknown variable")
        elif var_list[1].isalnum() and all(char.isdigit() for char in var_list[1]):
            variable_dict[var_list[0]] = var_list[1]
        else:
            print("Invalid assignment")
    elif var_list[0].isalnum() and not var_list[0].isalpha() and not var_list[0].isnumeric():
        print("Invalid identifier")



run = True
variable_dict = {}
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
    elif ("+" not in user_input and "-" not in user_input) or "=" in user_input:
        if "=" in user_input:
            if user_input.count("=") > 1:
                print("Invalid assignment")
            else:
                variables = [char.strip() for char in user_input.split("=")]
                variable_store(variables)
        elif user_input in variable_dict:
            print(variable_dict[user_input])
        elif user_input not in variable_dict:
            print("Unknown variable")
        else:
            print("Invalid identifier")
    else:
        numbers = user_input.split()
        arithmetic_function(numbers)
