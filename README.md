The Max Bank project is a simple yet functional console‑based banking system built using Python and object‑oriented programming principles. 
It mainly has 3 Classes,
  1. Bank Class -> which gives out the main Menu for the Customer/Admin to choose from.
  2. Customer Class -> Where the Customer can create or alter their account details.
  3. Admin Class -> gives Admin the Access to change the details or delete a Customer.

main.py
  - It presents users with a clean, interactive menu that allows them to create new accounts, check their balances, withdraw or deposit money, or access admin‑level features.
  - Each option is handled through dedicated methods, and the system continuously returns to the main menu, creating a smooth and uninterrupted user experience.

customer.py
  - It loads and updates customer records stored in a JSON file, ensuring data is persistent across sessions.
  - The class supports creating new accounts, including verifying age, account type, and minimum deposit requirements.
  - It allows customers to check balances, deposit money, and withdraw funds, updating the JSON file after every change.
  - Overall, the script acts as the data management backbone of the banking system, handling user input, validation, and secure record updates

admin.py
  - It uses fixed admin credentials — **Admin ID: 1100001 and Password: 'bank_manager'** — to authenticate users before granting admin access.
  - After successful login, the admin menu allows the administrator to view, edit, or delete customer details.
  - The edit function supports updating key fields such as first name, last name, age, country, and account type, with validation applied where necessary.
  - The delete function permanently removes a customer’s record from the JSON file.


