from customer import Customer
import json

admin_id = 1100001
admin_pwd = 'bank_manager'

class Admin(Customer):
    def admin_login(self):
        """
        Handles admin login by validating admin ID and password.

        :param self: Admin instance
        """

        adminID_input = input('Admin ID : ')
        adminPwd_input = input('Admin password: ')
        if int(adminID_input) == admin_id:
            if str(adminPwd_input) == str(admin_pwd):
                self.admin_menu()
        else:
            print('your Admin ID is wrong. Please try again')
            self.admin_login()

    def admin_menu(self):
        """
        Displays admin menu and routes to selected admin operations.

        :param self: Admin instance
        :return: None or 0 when exiting admin mode
        """
        while True:

            print("""
            Please choose from the below options
            1. View Customer details
            2. Edit Customer details
            3. Delete customer details
            4. Exit Admin Mode
                """)
            adminoption = input("your option: ")

            # Validate numeric input
            try:
                adminoption = int(adminoption)
            except ValueError:
                print("Please enter a valid number.")
                continue

            # Route based on admin selection
            if adminoption == 1:
                print('You can now view the personal details of Customers')
                self.admin_view()

            elif adminoption == 2:
                # Fetch customer data before editing
                cust_data = self.get_details_CustomerID()
                self.admin_edit(cust_data)

            elif adminoption == 3:
                self.admin_delete()

            elif adminoption == 4:
                print('Exit the Admin Mode')
                return 0  # Exit admin mode

            else:
                print("Please select from the given options only")

    
    def admin_edit(self,cust_data):
        """
        Allows admin to edit selected fields of a customer's details.

        :param self: Admin instance
        :param cust_data: Dictionary containing customer details
        :return: 0 when exiting edit mode
        """

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
            6. Exit edit mode (save the customer details)
            """)

            try:
                editOption = int(input("your option: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if editOption in options:
                option_key, field_value = options[editOption]

                # Age requires validation
                if editOption == 3:
                    value_change = self.age_verification()
                else:
                    value_change = input(
                        f'Please enter the new {option_key} for customer ID {cust_data["id"]}: '
                    )

                # Update the selected field
                cust_data['personal_details'][field_value] = value_change

            elif editOption == 6:
                # Save changes and exit edit mode
                self.update_details_CustomerID(cust_data)
                return 0

            else:
                print("Please select from the given options only")
                     
    
    def admin_delete(self):
        """
        Deletes a customer record based on customer ID.

        :param self: Admin instance
        :return: 0 when deletion is successful
        """
       
        cust_id = input("Please enter the Customer ID: ")

        for i in range(len(self.jsonData)):
            if int(self.jsonData[i]['id']) == int(cust_id):
                self.jsonData.pop(i)
                with open('customer_data.json','w') as file:
                    # Save updated list to file
                    json.dump(self.jsonData,file,indent=4)
                print(cust_id,' ID Customer account is deleted')
                return 0
        print("Given Customer ID is wrong.")
        self.admin_delete()
    

    def admin_view(self):
        """
        Retrieves and displays customer details for a given customer ID.

        :param self: Admin instance
        """

        cust_id = self.get_details_CustomerID()
        self.print_customer_details(cust_id)

        


        



