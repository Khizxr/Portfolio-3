#!/usr/bin python 3
"""""""""""
name = input("Enter your name: ")
if name:
	print("Your name is", name)
else:
	print("Hello Stranger")

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
password = input("Enter your password")


while True:
	if password in BAD_PASSWORDS:
		print("Common password used")
		password = input("Enter your password")
	if len(password) < 8:
		print("Your password is not long enough")
		password = input("Enter your password")
	elif len(password) > 12:
		print("Your password is too long")
		password = input("Enter your password")
	else:
		print("Your password is sufficient in length")
	break
password2 = input("Confirm your password")
if password2 == password:
	print("Congratulation. New password is set")
else:
	print("Passwords do not match")

"""""
num = int(input("Enter the multiplication"))

if num < 0:
	for count in range(-12, 0):
		print(num, 'x', count, '=', num * count)
else:
	for count in range(0, 13):
		print(num, 'x', count, '=', num * count)


