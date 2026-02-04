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
        3. Exit Admin Mode
              """)
        adminoption = input("your option: ")
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
            self.admin_menu()
    
    def admin_edit(self,cust_data):

        options = {
        1: ("First Name", "first_name"),
        2: ("Last Name", "last_name"),
        3: ("Age", "age"),
        4: ("Country", "country"),
        5: ("Account type", "acc_type"),
        }
     
        while True:
            print("""
            Choose what you want to edit for the Customer 
            1. First Name
            2. Last Name
            3. Age
            4. Country
            5. Account type
            6. Exit edit mode(save the customer details)
            """)
            try:
                editOption = int(input("your option: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if editOption in options:
                option_key, field_value = options[editOption]
                if editOption == 3:
                    print(f'For the customer ID {cust_data['id'] } new')
                    value_change = self.age_verification()
                else:
                    value_change = input(f'Please enter the new {option_key} for customer ID {cust_data['id']}: ')

                cust_data['personal_details'][field_value] = value_change

            elif editOption == 6:
                self.update_details_CustomerID(cust_data)
                return 0
            else:
                print("Please select from the given options only")
                     
    
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
        


        



