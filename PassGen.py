#!/bin/python3
#Password generator in Python

#import random function
import random

#possible chars to be randomly picked for our password
char="abcdefghijklmnopqrstuvwxyz1234567890?!@#$%"

size= input("how long would you like the password to be?")
size= int(size)
password = ""

#iterate size times
for x in range(size):
  password += random.choice(char)
print(password)
