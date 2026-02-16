from customer import Customer
from admin import Admin


class Bank(Admin):

    def menu_display(self):
        """
        Displays the main banking menu and returns the user's selected option.

        :param self: Bank instance
        :return: User-selected menu option as string
        """

        print("""
        ###########################
        Welcome to Max Bank.
        1. Create an account
        2. Check Balance
        3. Withdraw
        4. Deposit
        5. Admin Login
        6. Exit
        """)
        menuOption = input("your option:")
        return menuOption
    
    def Index(self):
        """
        Main loop for the banking system. Routes user input to the correct operation.

        :param self: Bank instance
        :return: None or 0 when exiting the program
        """

        while True:
            try:
                option = int(self.menu_display())
            except ValueError:
                print("Please enter a valid number.")
                continue

            #  Route based on user selection
            if option == 1:
                self.create_account()

            elif option == 2:
                self.check_balance()

            elif option == 3:
                self.withdraw()

            elif option == 4:
                self.deposit()

            elif option == 5:
                print("Please give your admin login credentials")
                self.admin_login()

            elif option == 6:
                print("Thank you for working with Max Banks")
                break  # Exit the loop and end the program

            else:
                print("Please select from the given options only")



# Program entry point
if __name__ == "__main__":
    bank_obj = Bank()
    bank_obj.Index()

