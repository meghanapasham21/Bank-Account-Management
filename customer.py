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
        self.age = self.age_verification()
        self.country = input(str("Country: "))
        self.account_type = input(str("Account Type: Savings(s)/ Current(c): "))
        self.reply = self.acc_type_verification(self.account_type)
        if self.reply == 'Y':
            self.balance = self.change_min_bal(self.account_type)
        else:
            if self.account_type =='c':
                self.balance = 200
            else:
                self.balance = 500
        print("Thank you. Your Account is created")
        self.customer_id  += 1
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

    def print_customer_details(self):

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
    
    def age_verification(self):

        while True:
            try:
                Age = input("Age:")
            except ValueError:
                print("Invalid input. Please enter a number.")

            if int(Age) > 80 or int(Age) < 18:
                print('A person who is aged only above 18 or below 80 are allowed to create an account')
            else:
                return Age
    
    def change_min_bal(self, acc_type):
            initial_amt = input("Please enter the initial deposit amount: ")
            if acc_type == 'c' and int(initial_amt) >= 200:
                return int(initial_amt)
            elif acc_type == 's' and int(initial_amt) >= 500:
                return int(initial_amt)
            else:
                print('Please make sure the initial amount you give is more than the minimum initial balance')
                self.change_min_bal(acc_type)
