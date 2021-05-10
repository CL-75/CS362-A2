# Name: Casey Levy
# CS 362 - A2 - Test Driven Development
# Description: Creating and executing several tests for
#   check_pwd.py program and implementing Test Driven Development

from check_pwd import check_pwd
import unittest

# Class for password check tests
class TestCase(unittest.TestCase):

# Testing for empty string
	def test1(self):
		pwd = ''
		self.assertFalse(check_pwd(pwd))

# Checking for all digits, invalid length of 6
	def test2(self):
		pwd = '123456'
		self.assertFalse(check_pwd(pwd))
		
# Checking for all uppercase letters, invalid length of 7
	def test3(self):
		pwd = 'ABCDEFG'
		self.assertFalse(check_pwd(pwd))

# Checking for all lowercase letters, invalid length of 7 
	def test4(self):
		pwd = 'abcdefg'
		self.assertFalse(check_pwd(pwd))

# Checking for combo upper and lowercase letters, invalid length of 7
	def test5(self):
		pwd = 'abcDEFG'
		self.assertFalse(check_pwd(pwd))

# Checking for fully valid password and valid length of 11
# check_pwd.py should return True for this even if this is an assertFalse
	def test6(self):
		pwd = 'abcDEFG123!'
		self.assertTrue(check_pwd(pwd))

# Checking for upper, lowercase, and digits, valid length of 9
	def test7(self):
		pwd = 'abcDEF123'
		self.assertFalse(check_pwd(pwd))

# Checking for valid password except with invalid symbols
	def test8(self):
		pwd = 'abcDEF123[]'
		self.assertFalse(check_pwd(pwd))

if __name__ == '__main__':
    unittest.main()