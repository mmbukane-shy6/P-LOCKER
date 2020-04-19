class Credentials:
    """
    A class that generates new instances for users
    """
    Credentials_list = []

    def __init__(self, acc_name, acc_email, acc_password):
        self.acc_name = acc_name
        self.acc_email = acc_email
        self.acc_password = acc_password

    def save_credentials(self):
        """
        save credentials list into credentials list array
        """
        Credentials.credentials_list.append(self)

    def delete_account(self):
        """
        method that allows application to delete accounts
        """
        Credentials.credentials_list.remove(self)
    @classmethod
    def display_credentials(cls):
         """
         method that returns the class array
         """
         return cls.Credentials_list