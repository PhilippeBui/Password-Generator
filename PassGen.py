#!/bin/python3
#Password generator in Python

#import random function
import random

#possible chars to be randomly picked for our password
char="abcdefghijklmnopqrstuvwxyz1234567890?!@#$%"

#user input for size of password
size= input("how long would you like the password to be?")
size= int(size)

#user input for how many passwords
pnum = input("how many passwords?")
pnum= int(pnum)

#iterate to number of passwords needed
for x in range(pnum):
  password = ""
#iterate to size of passwords
  for x in range(size):
    password += random.choice(char)
  print(password)
