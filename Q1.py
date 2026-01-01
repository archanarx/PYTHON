# Write a program to print N rows in the following pattern
# *
# **
# ***

n = int(input("Enter number of rows: "))
for i in range (1, n + 1 ):
    print ("*" " " * i)