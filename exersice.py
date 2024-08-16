#Ex1 - String 
# Enter text and display it one by one

# text = input("Enter text: ")
# for char in text:
#     print(char)

# Ex2 - String
# Enter text and display number of letter

# text = input("Enter text: ")
# for i in range(len(text)):
#     print(i)

# Ex3 - String
# Enter text and check if it contains capital letter or not

# text = input("Enter your text: ")
# output = "No"
# for i in range(len(text)):
#     if text[i].isupper():
#         output = "Yes"
# print(output)

# Ex4 - String 
# We have text = "3 4 5 6"
# Q1 - display number 1 by one without space
# Q2 - Sum all number (Total: 18)

# Q1
# text = "3 4 5 6"
# result = ""
# for char in text:
#     if char != " ":
#         result += char
# print(result)

# Q2
# text = "3 4 5 6"
# sum = 0
# for char in text:
#     if char != " ":
#         sum += int(char)
# print(sum)

# Ex5 - String 
# We have text = "454639"
# Q1 - Count odd and even number in text
# Q2 - Sum all number 
# Q3 - Sum only even number 
# Q4 - Reverse 

# Q1
# text = "454639"
# countEven = 0
# countOdd = 0
# for char in text:
#     if int(char) % 2 == 0:
#         countEven += 1
#     elif int(char) % 2 != 0:
#         countOdd += 1
# print("Even number = ", countEven)
# print("Odd number = ", countOdd)

# Q2
# text = "454639"
# sum = 0
# for char in text:
#     sum += int(char)
# print(sum)

# Q3
# text = "454639"
# sum = 0
# for char in text:
#     if int(char) % 2 == 0:
#         sum += int(char)
# print(sum)

# Q4
# text = "454639"
# reverse = ""
# for i in range(len(text)):
#     reverse += text[len(text) - 1 - i]
# print(reverse)

#Ex6 - Number
# Enter number and check 
# if odd number print "Odd" otherwise print "Even"

# num = input("Enter number: ")
# for char in num:
#     if int(char) % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

#Ex7 - number
# Enter number in range 10 - 20 until you enter other number out of range
# display "Continue" if number in range 10 - 20
# display "Out of range" if number difference from range 10 - 20

# num = int(input("Enter number: "))
# if num >= 10 and num <= 20:
#     print("Countinue")
# else:
#     print("Out of range")

#Ex8 - String
# We have text = "9394884039"
# Q1 - How many number 8 in string
# Q2 - What is first index of letter 8

#Q1
# text = "9394884039"
# sum = 0
# for char in text:
#     if int(char) == 8:
#         sum += 1
# print("Count number 8 =",sum)

#Q2
# text = "9394884039"
# isFound = False
# index = 0
# while not isFound:
#     if int(text[index]) == 8:
#         isFound = True
#     else:
#         index += 1
# print(index)

#Ex9 - String
# We have string = "3 4 5 6"
# Q1 - Remove space and keep result = "3456"
# Q2 - Multiple each letter by 2 result = "6 8 10 12"

#Q1
# string = "3 4 5 6"
# sum = ""
# for char in string:
#     if char != " ":
#         sum += char
# print(sum)

#Q2
# string = "3 4 5 6"
# result = ""
# for char in string:
#     if char != " ":
#         result += str(int(char) * 2) + " "
# print(result)

#EX10
# max = 0
# min = 0
# for i in range(5):
#     num = int(input("Enter number: "))
#     if i == 0:
#         max = num
#         min = num
#     else:
#         if num > max:
#             max = num
#         if num < min:
#             min = num
# print("Max =", max)
# print("Min =", min)
