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
    
