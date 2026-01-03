from customer import Customer
import json

admin_id = 1100001
admin_pwd = 'bank_manager'

class Admin(Customer):
    def admin_login(self):
    
        adminID_input = input('Admin ID : ')
        adminPwd_input = input('Admin password: ')
        if int(adminID_input) == admin_id:
            if str(adminPwd_input) == str(admin_pwd):
                self.admin_menu()
        else:
            print('your Admin ID is wrong. Please try again')
            self.admin_login()

    def admin_menu(self):

        print("""
        Please choose from the below options
        1. Edit Customer details
        2. Delete customer details
              """)
        adminoption = input(' ')
        if True:
            match int(adminoption):
                case 1:
                    print('You can now edit the personal details of Customers')
                    cust_data = self.get_details_CustomerID()
                    self.admin_edit(cust_data)
                case 2:
                    self.admin_delete()
                case 3:
                    print('Exit the Admin Mode')
                    return 0 
                case _:
                    print("Please select from the given options only")
                    self.admin_menu()
    
    def admin_edit(self,cust_data):
        
        print("""
        Choose what you want to edit
        1. First Name
        2. Last Name
        3. Age
        4. Country
        5. Account type
        6. Exit edit mode(save the customer details)
        """)
        editOption = input('')
        if True:
            match int(editOption):
                case 1:
                    print('Enter the new First name for Customer ID ', cust_data['id'])
                    firstName_edit = input('')
                    cust_data['personal_details']['first_name'] = firstName_edit
                case 2:
                    print('Enter the new Last name for Customer ID ', cust_data['id'])
                    lastName_edit = input('')
                    cust_data['personal_details']['last_name'] = lastName_edit
                case 3:
                    print('Enter the new age for Customer ID ', cust_data['id'])
                    age_edit = input('')
                    cust_data['personal_details']['age'] = age_edit
                case 4:
                    print('Enter the new country for Customer ID ', cust_data['id'])
                    customer_edit = input('')
                    cust_data['personal_details']['country'] = customer_edit
                case 5:
                    print('Enter the new account type for Customer ID ', cust_data['id'])
                    accountType_edit = input('')
                    cust_data['personal_details']['acc_type'] = accountType_edit
                case 6:
                    self.update_details_CustomerID(cust_data)
                    print('You exited the Admin mode')
                    self.Index()
                    return 0                                
                case _:
                    print("Please select from the given options only")
                    self.admin_menu()
            self.admin_edit(cust_data)
    
    def admin_delete(self):
        
        cust_id = input("Please enter the Customer ID: ")

        for i in range(len(self.jsonData)):
            if int(self.jsonData[i]['id']) == int(cust_id):
                self.jsonData.pop(i)
                with open('customer_data.json','w') as file:
                    json.dump(self.jsonData,file,indent=4)
                print(cust_id,' ID Customer account is deleted')
                return 0
        print("Given Customer ID is wrong.")
        self.get_details_CustomerID()
        


        



