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
		
