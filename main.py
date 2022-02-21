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

## WK 4 CHALLENGE 7

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


## WK 4 CHALLENGE 8

# name = str(input("What is your name?  ")).upper()
# name_reverse = ""
# index = len(name) 
# while index > 0: 
#     name_reverse += name[index - 1] 
#     index = index - 1 
# print(name_reverse)

## WK 4 CHALLENGE 9

# def cube(num1):
#   num_cube = num1 ** 3
#   return num_cube

# num1 = float(input("Enter a number."))
# total = cube(num1)
# print(total)

## WK 4 CHALLENGE 10

# num1 = float(input("Enter a number."))

# for r in range(1,13):
#   total = num1 * r
#   print(f"{num1} * {r} = {total}")

## WK 4 CHALLENGE 11

# def product(num1,num2):
#   total = num1 * num2
#   return total

# num1 = float(input("Enter a number."))
# num2 = float(input("Enter a second number."))
# result = product(num1,num2)

# print(f"Your total is {result}.")

## WK 4 CHALLENGE 12

# def multi(num1,num2):
#   product = num1 * num2
#   return product

# def addto(product,num3):
#   sum = product + num3
#   return sum

# num1 = float(input("Enter a number. "))
# num2 = float(input("Enter a second number. "))
# product = multi(num1,num2)

# num3 = float(input("Enter a third number. "))
# sum = addto(product,num3)

# print(f"Your result is: \n{num1} * {num2} + {num3} = {sum}.")

## WK 4 CHALLENGE 13

# def add(num1,num2):
#   total = num1 + num2
#   return total

# ask = True
# round = 0

    
# while ask == True:
#   if round == 0:
#     num1 = float(input("Enter a number: "))
#   else:
#     num1 = total
#   num2 = float(input("Enter another number: "))
#   total = add(num1,num2)
#   print(total)
#   round += 1


'''Leaving for reference of what not to do   
# while ask == True:
#   if round == 0:
#     num1 = float(input("Enter a number: "))
#     num2 = float(input("Enter a second number: "))
#     total = add(num1,num2)
#     print(total)
#     round += 1

#   elif round > 0:
#     # num1 = total 
#     num2 = float(input("Enter a new number: "))
#     new_total = add(total,num2)
#     print(new_total)
#     round += 1'''


## WK 4 CHALLENGE 14

# colors = ["void", "infrared", "red", "orange", "yellow", "green", "blue", "indigo", "violet", "ultraviolet"]

# for color in colors:
#   print(color)


## WK 4 CHALLENGE 15

# number = input("Enter your score. ")
# grade = float(number)
     
# if grade >= 0 and grade <= 70:
#   is_passing = False
# elif grade > 70 and grade <= 100:
#   is_passing = True

# if is_passing == False:
#   print("F A I L I N G")
# else:
#   print("Passing!")


## WK 4 CHALLENGE 16

# start = int(input("Enter your starting number. "))
# stop = int(input("Enter your final number. "))
# total = 0

# range_stop = stop + 1
# your_range = range(start, range_stop)

# for r in range(start,range_stop):
#   total = r + total
#   r += 1

# print(total)

# '''NOTES'''# print(len(your_range))
# # print(your_range[5])

## WK 4 CHALLENGE 17

# for r in range(100,-1,-1):
#   print(r)
#range(start,stop,step)
'''I know this program works, but replit is acting up. Again.'''

# # WK 4 CHALLENGE 18

# alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# letter = input("Enter a letter. ").upper()

# if letter in alphabet:
#   number = alphabet.index(letter)
#   print(f"The index is {number}.\n{letter} is number {number+1} in the alphabet.")
# else:
#   print("That is not a letter.")

# # WK 4 CHALLENGE 19

# def opp(num1,num2,num3,num4):
#   total = (num1 / num2 * num3)-num4
#   return total

# num1 = float(input("Enter a number. "))
# num2 = float(input("Enter another number. "))
# num3 = float(input("Enter another number. "))
# num4 = float(input("Enter another number. "))

# result = opp(num1, num2, num3, num4)
# print(f"{result} is your result.")

# # WK 4 CHALLENGE 20

# def determine(num1):
#   modulus = num1 % 2
#   if modulus == 0:
#     num1 = "even"
#   else:
#     num1 = "odd"
#   return num1
#   # return modulus --> Don't do this. It wil return "1" or "0", not "even"/"odd"

# num1 = int(input("Enter an integer. "))
# result = determine(num1)
# print(f"{num1} is {result}.")

# # WK 4 CHALLENGE 21

# def is_prime(num1):
#   if num1 == 1:
#     result = "neither prime or composite"
#     return result
#   # if num1 == 2:
#   #   num1 = "prime"
#   #   return num1
#   elif num1 > 1 :
#     for r in range(2, (num1//2)+1):
#       if num1 % r == 0:
#         result = "composite"
#         return result
#     else: #all I needed to do was shift this left!
#       result = "prime"
#       return result  

# run = True

# while run == True:
#   num1 = int(input("Enter a positive integer. "))
#   result = is_prime(num1)
#   print(f"{num1} is {result}.")

# # WK 4 CHALLENGE 22

# def determine(number):
#   if number % 2 == 0:
#     is_odd = False
#     return is_odd
#   else:
#     is_odd = True
#     return is_odd

# num1 = int(input("Enter your minimum number: "))
# num2 = int(input("Enter your maximum number: "))

# for i in range(num1,num2+1):
#   is_odd = determine(i)
#   if is_odd == True:
#     print(i)

# # WK 4 CHALLENGE 23
