# Question 1: Print 1 to N (For Loop)
#
# Question: Take an integer N and print numbers from 1 to N.
#
# Input: 5
# n=int(input("enter the number"))
# for i in range(1,n+1):
#     print(i,end=" ")
#     print()
# Question 2: Print N to 1 (While Loop)
#
# Question: Print numbers from N down to 1.
#
# Input: 5
# n=int(input("enter the number"))
# for i in range(5,0,-1):
# #     print(i)
# i=5
# while i>0:
#     print(i)
#     i=i-1
# n=int(input("enter the number"))
# while n>0:
#     print(n)
#     n=n-1
# Question 3: Sum of First N Numbers
#
# Question: Find the sum of first N natural numbers.
# n=int(input("enter the number"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print("sum is:",sum)
# factorial
# n=int(input("enter the number"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# # print(fact)
# Question 5: Reverse a Number (While)
#
# Question: Reverse a given number.
#
# Input: 1234
#
# Output:
#
#
# n=int(input("enter the number"))
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# print(rev)Question 6: Check Prime Number
#
# Question: Check whether a number is prime
# n=int(input("enter the number"))
# for i in range(2,n):
#     if n%i==0:
#         print("it is not prime")
#         break
# else:
#       print("it is prime")
# Question: Print multiplication table of a given number.
#
# Input: 5

# n=int(input("enter the number"))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)
# Question: Count the number of digits.
#
# Input: 12345
# n=int(input("enter the number"))
# count=0
# while n>0:
#     digit=n%10
#     count+=1
#     n=n//10
# print(count)
# n=int(input("enter the number"))
# a,b=0,1
# for i in range(n):
#     print(a,end="")
#     a,b=b,a+b

# for i in range(1,6,-1):
#     for j in range(-i):
#         print(i,end=" ")
#     print()
# Try these in 20 minutes like an online assessment.
#
# Print even numbers from 1 to 100.
#
# Find the largest digit in a number.
#
# Find the sum of digits.
#
# Check whether a number is an Armstrong number.
#
# Print all prime numbers between 1 and 100.
#
# Print this pattern:
# for i in range(1,101):
#     if i%2==0:
#       print(i)
# n = int(input("Enter the number: "))
# largest = 0
#
# while n > 0:
#     digit = n % 10
#
#     if digit > largest:
#         largest = digit
#
#     n = n // 10
#
# print("Largest digit is:", largest)
# n=int(input("enter number"))
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# print(sum)
# n = int(input("Enter a number: "))
# original = n
#
# count = len(str(n))
# total = 0
#
# while n > 0:
#     digit = n % 10
#     total = total + digit ** count
#     n = n // 10
#
# if total == original:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")
# for i in range(1,101):
#     for j in range(2,i):
#         if i%j==0:
#
#             break
#     else:
#           print(i,"is prime")
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# Reverse a string using a loop.
#
# Count vowels in a string
# string=input("enter a string")
#
# for i in range(0,len(string)):
#     rev=string[::-1]
# print(rev)
string=input("enter a string")
count=0
vowel="aeiou"
for i in string:
  if i in vowel:
    count+=1
print(count)





