#!/usr/bin/python3

password = []

with open('passwords.txt', 'r') as filehandle:
    password = [current_place.rstrip() for current_place in filehandle.readlines()]

for i in password:
	print("peter\n"+i)

