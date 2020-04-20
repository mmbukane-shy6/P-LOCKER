import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User("Sheila", "Egeidza",
                             "0796680568", "sheilaegeidza@gmail.com")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
    User.user_list = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
          """
        self.assertEqual(self.new_user.first_name, "Sheila")
        self.assertEqual(self.new_user.last_name, "Egeidza")
        self.assertEqual(self.new_user.phone_number, "0796680568")
        self.assertEqual(self.new_user.email, "sheilaegeidza@gmail.com.com")
    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into
         the users array
        """
    def test_save_user(self):
        """    
        test_save_user test case to test if the user object is saved into
         the users array
        """  
        self.new_user.save_user_details()
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_users(self):
        '''
        test_save_multiple_contact to check if we can save multiple users
        objects to our user_list
        '''
        self.new_user.save_user_details()
          test_user = User("Test", "Tester", "0714271014", "testuser@gmail.com")
         test_user.save_user_details()
        self.assertEqual(len(User.user_list), 2)

    def test_display_users(self):
        self.assertEqual(User.display_users(), User.user_list)
        
if __name__ == '__main__':
    unittest.main()
