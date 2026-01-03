import json
from json.decoder import JSONDecodeError

class Customer:

    def __init__(self):

        self.customer_dict = {}
        try:
            with open('customer_data.json','r') as file:
                self.jsonData = json.load(file)
        except FileNotFoundError:
            print("File not found!")
        except JSONDecodeError:
            print("Invalid JSON format!")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        
        if len(self.jsonData) == 0:
            self.customer_id = 1111001  
        else:
            self.customer_id = self.jsonData[-1]['id']

    """
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
        """

                
    def acc_type_verification(self, account_type):

        if self.account_type == 'c':
            self.reply = input(str("For Current Account the initial minimum deposit amount is 200.\nIf you want to add more amount, Please press Y. If not press N "))
        elif self.account_type == 's':
            self.reply = input(str("For Savings Account the initial deposit amount is 500.\nIf you want to add more amount, Please press Y. If not press N "))
        else:
            print("please give only s or c as options")
            self.reply = 'N'
        return self.reply

    def create_account(self):
        
        self.first_name = input(str("First Name:"))
        self.last_name = input(str("Last Name:"))
        self.age = input("Age:")
        if int(self.age) > 80 or int(self.age) < 18:
            print('A person who is aged only above 18 or below 80 are allowed to create an account')
            self.age = input("Age:")
        elif isinstance(self.age,int):
            print('Age can only be a number from 18 to 80')
            self.age = input("Age:")
        self.country = input(str("Country: "))
        self.account_type = input(str("Account Type: Savings(s)/ Current(c): "))
        self.reply = self.acc_type_verification(self.account_type)
        if self.reply == 'Y':
            self.balance = change_min_bal()
        else:
            print("Thank you. Your Account is created")
            self.customer_id  += 1
            if self.account_type =='c':
                self.balance = 200
            else:
                self.balance = 500
            print("your customer id is ", self.customer_id)

        self.customer_dict = {
            "id" : int(self.customer_id),
            "balance" : self.balance,
            "personal_details" : {
                "first_name" : self.first_name,
                "last_name" : self.last_name,
                "age" : self.age,
                "country" : self.country,
                "acc_type" : self.account_type
            }
        }

        self.jsonData.append(self.customer_dict)
        with open("customer_data.json","w") as output_file:
            json.dump(self.jsonData,output_file,indent=4)
        self.print_customer_details()

        def change_min_bal():
            initial_amt = input("Please enter the initial deposit amount: ")
            if self.account_type == 'c' and int(initial_amt) >= 200:
                bal = int(initial_amt)
            elif self.account_type == 's' and int(initial_amt) >= 500:
                bal = int(initial_amt)
            else:
                print('Please make sure the initial amount you give is more than the minimum initial balance')
                change_min_bal()
            return bal


    def print_customer_details(self):

        #with open("customer_data.json", "r") as read_file:
        #    cust_data = json.load(read_file)
        #    print(cust_data["id"])
 
        if self.customer_dict["personal_details"]["acc_type"] == 'c':
            acc_type = 'Current Account' 
        else:
            acc_type = 'Savings Account'

        print('Customer id: ',self.customer_dict["id"],
              '\nFirst name: ',self.customer_dict["personal_details"]["first_name"], 
              '\nLast name: ',self.customer_dict["personal_details"]["last_name"], 
              '\nAccount type: ',acc_type)
     
    def check_balance(self):

        data = self.get_details_CustomerID()
        print('Hello ',data["personal_details"]["first_name"],
              ' your Balance is: ', data['balance'])
        
    def withdraw(self):

        data = self.get_details_CustomerID()
        print(data)
        withdraw = input('Please enter the withdrawl amount: ')
        if int(withdraw) > data["balance"]:
            print("Insufficient Funds.")
            self.Index()
        else:
            data["balance"] -= int(withdraw)
            print(data["personal_details"]["first_name"],'your current balance is', data['balance'])
            self.update_details_CustomerID(data)       

    def deposit(self):

        data = self.get_details_CustomerID()
        deposit_amt = input('Please enter the deposit amount: ')
        data["balance"] += int(deposit_amt)
        print(data["personal_details"]["first_name"],'your current balance is', data['balance'])
        self.update_details_CustomerID(data)
    
    def get_details_CustomerID(self):

        cust_id = input("Please enter the Customer ID: ")

        for i in range(len(self.jsonData)):
            if int(self.jsonData[i]['id']) == int(cust_id):
                return self.jsonData[i]
        print("Given Customer ID is wrong.")
        self.get_details_CustomerID()
    
    def update_details_CustomerID(self,cust_data):

        for i in range(len(self.jsonData)):
            if int(self.jsonData[i]['id']) == cust_data['id']:
                self.jsonData[i]['balance'] = cust_data['balance']
                self.jsonData[i]['personal_details']['first_name'] = cust_data['personal_details']['first_name']
                self.jsonData[i]['personal_details']['last_name'] = cust_data['personal_details']['last_name']
                self.jsonData[i]['personal_details']['age'] = cust_data['personal_details']['age']
                self.jsonData[i]['personal_details']['country'] = cust_data['personal_details']['country']
                self.jsonData[i]['personal_details']['acc_type'] = cust_data['personal_details']['acc_type']
        with open('customer_data.json','w') as file:
            json.dump(self.jsonData,file,indent=4)
