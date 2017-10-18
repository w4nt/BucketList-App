"""Contains the User and BucketList classes"""

class User(object):
    """Handles the registration and logging in of users    
    
    Parameters:
    - email: Holds the e-mail address the user uses to register
      and log into the application
    - password: Holds the password the user submits during registration
      and logging into the application"""

    def __init__(self, email, password):
        self.user_db = {}
        self.email = email
        self.password = password

    def register_user(self):
        """Method to handle registration of users.
        - confirm_password: Holds the second entry of the password
          by the user."""
        self.email = input("Enter your e-mail address: ")
        self.password = input("Enter a password: ")
        confirm_password = input("Enter the password again: ")
        
        if self.email in self.user_db:
            print("You're already registered. Try logging in.")
        else:
            if self.password == confirm_password:
                print("Sorry, the two passwords don't match. Try again. ")
            else:
                self.user_db[self.email] = self.password

    def login_user(self):
        """Method to handle logging in of users."""
        self.email = input("Enter your e-mail address: ")
        self.password = input("Enter your password: ")
        if self.email in self.user_db and self.user_db[self.email] != self.password:
            print("You have entered the e-mail and/or wrong password. Please try again.")
        elif self.email in self.user_db and self.user_db[self.email] == self.password:
            print("Welcome. You've successfully logged in.")
        else:
            print("Are you sure you have an account with us?\n Please try registering.")

class BucketList(object):
    """This class contains the methods for interacting with the users'
    BucketLists"""

    def create_list(self):
        """This method creates the list"""
        pass

    def delete_list(self, parameter_list):
        """This method deletes the list"""
        pass

    def view_list(self, parameter_list):
        """This method views the list"""
        pass

    def update_list(self, parameter_list):
        """This method updates a list"""
        pass

    def add_list_item(self, parameter_list):
        """This method adds an item to a list"""
        pass

    def view_list_item(self, parameter_list):
        """This method views items in a list"""
        pass

    def delete_list_item(self, parameter_list):
        """This method deletes items from a list"""
        pass

    def update_list_item(self, parameter_list):
        """This method updates items in a list"""
pass
