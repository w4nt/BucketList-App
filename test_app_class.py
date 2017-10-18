from unittest import TestCase, main
from app_class import User

class UserTestCase(TestCase):
    """This is an instance of the Test Case class
    that will be used in testing the User class in
    app_class.py"""
    def setUp(self):
        self.my_user = User()
    
    def test_login_user(self):
        """A method to test the accuracy of the
        login method in the User class"""
        self.my_user.email = "isee@you.com"
        self.my_user.password = "password123"
        assertEqual(self.my_user.user_db[email], self.my_user.password,
                    msg='Password added successfully')
        assertTrue(self.my_user.user_db[email] == self.my_user.email,
msg='E-mail address added successfully') 
