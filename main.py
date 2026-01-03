"""
Create a new account and view account holders record.
Withdraws and deposit amount with the balance inquiry.
Closing an account and edit account details.
User can create an account by providing the name of the account holder, number, etc.
User can select the amount type (Saving or Current account).
They can also provide an initial amount more than or equal to 500.
He/She can modify their account detail and type if they want to.
"""
from customer import Customer
from admin import Admin


class Bank(Admin):
    def menu_display(self):

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
        option = int(self.menu_display())
        if True:
            match option:
                case 1:
                    self.create_account()
                case 2:
                    self.check_balance()
                case 3:
                    self.withdraw()
                case 4:
                    self.deposit()
                case 5:
                    print('Please give your admin login credentials')
                    self.admin_login()
                case 6:
                    print('Thank you for working with Max Banks')
                    return 0                    
                case _:
                    print("Please select from the given options only")
                    self.Index()
            self.Index()


bank_obj = Bank()
bank_obj.Index()    
    
    