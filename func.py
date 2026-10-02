# # def display_name():
# #     n=input("Enter your name: ")
# #
# #     print("hello",n)
# # display_name()
# #
# # def fact(n):
# #     fact=1
# #     for i in range(1,n+1):
# #         fact=fact*i
# #     return  fact
# # x=fact(6)
# # print(x)
# # def charcount(s,ch):
# #     count=0
# #     for i in s:
# #         if i==ch:
# #             count+=1
# #     return count
# # s="hello world"
# # ch="l"
# # print(charcount(s,ch))
# # def prime(n):
# #     for i in range(2,n):
# #         if n%i==0:
# #             return False
# #         else:
# #             return True
# # x=prime(5)
# # print(x)
# # def factors(n):
# #     for i in range(1,n+1):
# #         if n%i==0:
# #            print(i)
# # x=factors(12)
# # print(x)
# # def spy(n):
# #     s = 0
# #     p = 1
# #
# #     for i in str(n):
# #         s = s + int(i)
# #         p = p * int(i)
# #
# #     if s == p:
# #         return True
# #     else:
# #         return FalseQ1. Even or Odd
# #
# # Define a function:
# #
# # check_even(n)
# #
# # that accepts a number and returns whether it is even or odd.
# #
# # Example:
# # def check_even(n):
# #   for i in range(n):
# #     if n%2==0:
# #      return "even"
# #     else:
# #         return "odd"
# # n=check_even(3)
# # print(n)
# # def max(a,b):
# #     if a>b:
# #         return a
# #     else:
# #         return b
# # n=max(10,20)
# # print(n)
# # Q3. Sum of Digits ⭐
# #
# # Create:
# #
# # sum_digits(n)
# #
# # Example:
# #
# # Input: 12345
# # Output: 15
# #
# # Hint:
# #
# # for i in str(n):
# # def sumodgigits(n):
# #     sum=0
# #     for i in str(n):
# #         sum=sum+int(i)
# #     return sum
# # s=sumodgigits(123)
# # print(s)
# # Q4. Count Vowels ⭐⭐
# #
# # Create:
# #
# # count_vowels(s)
# #
# # Example:
# #
# # Input: "python programming"
# # Output: 3
# #
# # Don't use count().
# #
# # Use a loop.
# # def count_vowels(s):
# #     vowelscount=0
# #     vowel="aeiouAEIOU"
# #     for i in s:
# #         if i in vowel:
# #             vowelscount+=1
# #     return vowelscount
# # s=count_vowels("hello world")
# # print(s)
# # def reverse(s):
# #     rev=""
# #     for i in s:
# #         rev=i+rev
# #     return rev
# # s=reverse("keerthi")
# # print(s)
# # def pallindrome(s):
# #     rev=""
# #     original=s
# #     for i in s:
# #         rev=i+rev
# #     if rev==original:
# #         return"pallindrome"
# #     else:
# #         return"not pallindrome"
# # print(pallindrome("madam"))
# # def isprime(n):
# #     if n < 2:
# #         return False
# #
# #     for j in range(2, n):
# #         if n % j == 0:
# #             return False
# #
# #     return True
# #
# #
# # for i in range(1, 101):
# #     if isprime(i):
# #         print(i)
#
#
# # def armstrong(n):
# #     temp = n
# #     sum = 0
# #     count = 0
# #
# #     # count number of digits
# #     while temp > 0:
# #         count += 1
# #         temp = temp // 10
# #
# #     temp = n
# #
# #     # calculate Armstrong sum
# #     while temp > 0:
# #         digit = temp % 10
# #         sum = sum + digit ** count
# #         temp = temp // 10
# #
# #     if sum == n:
# #         return True
# #     else:
# #         return False
# #
# #
# # a = armstrong(153)
# # print(a)
# # def count_digit(n):
# #     count = 0
# #     while n>0:
# #         digit = n % 10
# #         count=count+1
# #         n=n//10
# #     return count
# # a=count_digit(103456667709)
# # print(a)
# # def sumeven(*args):
# #     sum=0
# #     for i in args:
# #         if i%2==0:
# #             sum+=i
# #     return sum
# # print(sumeven(2,9,4,1))
# Q13. Second Largest Number ⭐⭐⭐⭐
#
# Write a function:
#
# second_largest(numbers)
#
# that finds the second largest number in a list.
#
# Example:
#
# second_largest([10, 25, 7, 40, 18])
#
# Output:
#
# 25
#
# Try without using sort() or sorted().
# def second(l):
#    largest=l[0]
#    second=l[1]
#    for i in l:
#        if i>largest:
#           second=largest
#           largest=i
#        elif i>second:
#            second=i
#        return second
# l=[10,30,40]
# s=second(l)
# print(s)
# Write:
#
# char_frequency(s)
#
# that returns a dictionary containing the frequency of each character.
#
# Example:
#
# Input: "banana"
#
# Output:
# {'b': 1, 'a': 3, 'n': 2}
#
# Hint: use a dictiona
# def frequency(s):
#     d={}
#     for i in s:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1
#     return d
# a=frequency("banana")
# print(a)
# def strong(n):
#     original = n
#     sum = 0
#
#     while n > 0:
#         digit = n % 10
#
#         fact = 1
#         for i in range(1, digit + 1):
#             fact = fact * i
#
#         sum = sum + fact
#         n = n // 10
#
#     if original == sum:
#         return "Strong Number"
#     else:
#         return "Not Strong Number"
#
#
# a = strong(145)
# print(a)
# def anagram(s1,s2):
#     if len(s1)!=len(s2):
#         return False
#     d1={}
#     d2={}
#     for i in s1:
#         if i not in d1:
#             d1[i]=1
#         else:
#          d1[i]=d1[i]+1
#     for i in s2:
#         if i not in d2:
#             d2[i]=1
#         else:
#             d2[i]=d2[i]+1
#     if d1==d2:
#       return "ANAGRAM"
#     else:
#         return "NOT ANAGRAM"
# s1=input("Enter your first string: ")
# s2=input("Enter your second string: ")
# a=anagram(s1,s2)
# print(a)
# def movezeros(l):
#     new=[]
#     for i in l:
#         if i!=0:
#             new.append(i)
#     zerocount=l.count(0)
#     for i in range (zerocount):
#         new.append(0)
#     return new
#
# l=[1,0,8,0,9]
# a=movezeros(l)
# print(a)
# def removedup(l):
#     new=[]
#
#     for i in l:
#
#      if i not in new:
#         new.append(i)
#     return new
# l=[1,3,4,2,8,1,3]
# a=removedup(l)
# print(a)
# def repeat(s):
#     d={}
#
#     for i in s:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1
#     for i in s:
#         if d[i]==1:
#          return i
#
#     return "no "
#
# s="swiss"
# a=repeat(s)
# print(a)
# def missing_number(l):
#     n = len(l) + 1
#
#     expected = n * (n + 1) // 2
#
#     actual = 0
#
#     for i in l:
#         actual += i
#
#     return expected - actual
#
#
# l = [1, 2, 3, 5, 6]
#
# print("Missing number:", missing_number(l))














