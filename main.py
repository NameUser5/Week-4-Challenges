# #WK 4 CHALLENGE 1 
# def add(num1, num2):
#   num_sum = num1 + num2
#   return num_sum
  
# num1 = 12
# num2 = 12
# total = add(num1,num2)

# print(total)

# #WK 4 CHALLENGE 2
# def add(num1,num2):
#   num_sum = num1 + num2
#   return num_sum

# num1 = "12"
# num2 = "12"
# total = add(num1,num2)

# print(total)

# #WK 4 CHALLENGE 3

# ask_num = int(input("Enter a number."))
# num_convert = str(ask_num)

# print(num_convert)
# print(type(num_convert))

# #WK 4 CHALLENGE 4

# #LEVEL 1
# your_name = input("What is your name? ")
# print(f"Hello, {your_name}")

# #LEVEL 2
# is_valid = False

# while is_valid == False:
#   name = input("What is your name? ")  
#   if name.isalpha():
#     is_valid = True
#     name = name.capitalize()
#     print(f"Hello, {name}.")
#   else:
#     not name.isalpha()
#     name = print("Letters only. ")

# #WK 4 CHALLENGE 5

# #LEVEL 1

# name = input("What is your name? ").upper()
# print(name)

# #LEVEL 2

# is_valid = False

# while is_valid == False:
#   name = input("What is your name? ")
#   if name.isalpha():
#     is_valid = True
#     name_cap = name.upper()
#     print(f"Hi, {name_cap}.")
#   else:
#     print("Enter letters only.")

# #WK 4 CHALLENGE 6

# asking_name = True

# while asking_name == True:
#   name = str(input("What is your first name? "))
#   if name.isalpha():
#     asking_name = False
#     letter_count = len(name)
#     print(f"You have {letter_count} letters in your first name.")
#   else:
#     print("Letters only. First name only.")

# #WK 4 CHALLENGE 7

# def last_two(name):
#   print(name[-2],name[-1])

# ask = True

# while ask == True:
#   name = input("Enter your first name. ")
#   if name.isalpha():
#     ask = False
#     lname = last_two(name)  #because print is already used in your function, do not put again, othwerwise Python will print the last two letters AND try to do the same with the print function used here (hence "None")!
#   else:
#     print("Your first name, please!")


#WK 4 CHALLENGE 8