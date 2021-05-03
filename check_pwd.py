# Name: Casey Levy
# CS 362 - A2 - Test Driven Development
# Description: Creating and executing several tests for
#   check_pwd.py program and implementing Test Driven Development


def check_pwd(pwd):
	digit_count = 0
	upper = 0
	lower = 0
	sym = '~`!@#$%^&*()_+-='
	sym_count = 0

# First checking to ensure valid length
	if len(pwd) < 8 or len(pwd) > 20:
		return False

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

# Check for all lowercase letters
	for x in pwd:
		if x.islower():
			lower += 1

# Check for symbols
	for x in pwd:
		for y in sym:
			if x == y:
				sym_count += 1
				return True
			else:
				return False

	if upper == 0:
		return False
	if lower == 0:
		return False
	if digit_count == 0:
		return False

	return True


