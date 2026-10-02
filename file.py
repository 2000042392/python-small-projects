# # Q1. Write a Python program to count the number of lines in a file.
# f=open("k.txt","r")
# s=f.readlines()
# print(len(s))
f = open("k.txt", "r")
s = f.readlines()
f.close()

s[0] = "java\n"

f = open("k.txt", "w")
f.writelines(s)
f.close()
