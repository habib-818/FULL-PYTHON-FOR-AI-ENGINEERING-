## WHAT IS WHILE LOOP?
"""
 A while loop is used to repeat a block of code as long as a condition is True.
"""

# 01: BASIC SYNTEX
'''
   while condition:
       Code to execute
'''

# 02: COUNT FROM 1 TO 5
count = 1

while count <= 5:
    print(count)
    count += 1

# 03: ASK UNTILL THE CORRECT ANSWER
password = ""

while password != "python":
    password = input("Enter the password: ")

print("Access granted!")