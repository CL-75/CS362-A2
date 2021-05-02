# Name: Casey Levy
# CS 362 - A2 - Test Driven Development
# Description: Creating and executing several tests for
#   check_pwd.py program and implementing Test Driven Development


def check_pwd(pwd):
	digit_count = 0
	upper = 0
# Check for empty string, returns False if true
	if pwd == '':
		return False

# Check for all digits 
	for x in pwd:
		if x.isdigit():
			digit_count += 1

# Check for all uppercase letters
	for x in pwd:
		if x.isupper():
			upper += 1


