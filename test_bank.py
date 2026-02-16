import json
import pytest
from customer import Customer
from admin import Admin
from unittest.mock import MagicMock, patch


@pytest.fixture
def customer_json_env(tmp_path, monkeypatch):
    #Creates a temporary customer_data.json file and changes the working directory to the temporary folder.

    data = []
    json_file = tmp_path / "customer_data.json"
    json_file.write_text(json.dumps(data))

    monkeypatch.chdir(tmp_path)

    return data, json_file


def test_json_file_exists(customer_json_env):
    #checks if the json is readable
    
    cust_data, json_file = customer_json_env
    cust_data = [{'id': 200, 'name': 'Meghana'}]
    json_file.write_text(json.dumps(cust_data))

    #Instantiate Customer (it should load the fake JSON)
    Cust = Customer()

    assert Cust.jsonData == cust_data 
    assert Cust.customer_id == 200

def test_file_empty(customer_json_env):
    #checks, if the json file is empty then the customer ID is assigned to 1111001"
    
    data, json_file = customer_json_env
    #Instantiate Customer (it should load the fake JSON)
    Cust = Customer()
    assert Cust.customer_id == 1111001

def test_customer_acc_creation(customer_json_env, monkeypatch):
    #to test if the customer account is properly created 

    data, file_path = customer_json_env

    # Mock an input as custoer details in an iterator
    cust_mock_inputs = iter(['Meghana','Pasham','India','s'])

    monkeypatch.setattr("builtins.input", lambda _: next(cust_mock_inputs))
    monkeypatch.setattr(Customer,"age_verification", lambda self: "25")
    monkeypatch.setattr(Customer, "acc_type_verification", lambda self, acc_type : "N")

    cust = Customer()
    cust.create_account()

    assert len(cust.jsonData) == 1

    #assign the json data to a variable to verify if the json file is updated right
    cust_data_json = cust.jsonData[0]
    
    assert cust_data_json["personal_details"]["first_name"] == "Meghana"
    assert cust_data_json["personal_details"]["last_name"] == "Pasham"
    assert cust_data_json["personal_details"]["age"] == "25"
    assert cust_data_json["personal_details"]["country"] == "India"
    assert cust_data_json["personal_details"]["acc_type"] == "s"
    assert cust_data_json["balance"] == 500  # minimum for savings'\

def test_extra_deposit(customer_json_env, monkeypatch):
    #to check when customer wants to add extra deposit amount during account creation
    
    data, file_path = customer_json_env
    cust_mock_inputs = iter(["Rudransh", "Putta", "Germany", "c"])
    monkeypatch.setattr("builtins.input", lambda _: next(cust_mock_inputs))
    monkeypatch.setattr(Customer,"age_verification", lambda self: "25")
    monkeypatch.setattr(Customer, "acc_type_verification", lambda self, acc_type : "Y")
    monkeypatch.setattr(Customer, "change_min_bal", lambda self, initial_amt : "300")
    monkeypatch.setattr(Customer, "print_customer_details", lambda self, d: None)

    cust = Customer()
    cust.create_account()

    #now verify the json data if it got populated 
    assert len(cust.jsonData) == 1

    #assign the json data to a variable to verify if the json file is updated right
    cust_data_json = cust.jsonData[0]
    
    assert cust_data_json["personal_details"]["acc_type"] == "c"
    assert cust_data_json["balance"] == "300"  # minimum for savings'\

def test_age_verification(customer_json_env, monkeypatch):
    #to check if wrong age is handled correctly

    cust_mock_inputs = iter(["10", "83", "25"])
    monkeypatch.setattr("builtins.input", lambda _: next(cust_mock_inputs))

    cust = Customer()
    age_result = cust.age_verification()

    assert age_result == "25"

@pytest.mark.parametrize(
    "initial, deposit, expected", 
    [(200, 50, 250),
     (250, 30, 280)
])
def test_deposit(monkeypatch, initial, deposit, expected):
    #to check if the deposit is adding the amount to the balance
    cust = Customer()
    mock_data = {
        "id": 1111004,
        "balance": initial,
        "personal_details": {"first_name": "Meghana"}}
    monkeypatch.setattr(Customer, "get_details_CustomerID", lambda self: mock_data)
    monkeypatch.setattr("builtins.input", lambda _: deposit)
    cust.update_details_CustomerID = MagicMock()

    cust.deposit()

    assert mock_data["balance"] == expected

@pytest.mark.parametrize(
    "initial, withdraw, expected", 
    [(200, 50, 150),
     (150, 30, 120),
     (200, 250, 200)
])
def test_withdraw(monkeypatch, initial, withdraw, expected):
    #to check if the withdraw is deducting the amount to the balance 
    
    cust = Customer()
    mock_data = {
        "id": 1111004,
        "balance": initial,
        "personal_details": {"first_name": "Meghana"}}
    monkeypatch.setattr(Customer, "get_details_CustomerID", lambda self: mock_data)
    monkeypatch.setattr("builtins.input", lambda _: withdraw)
    cust.update_details_CustomerID = MagicMock()

    cust.withdraw()

    assert mock_data["balance"] == expected

def test_check_balance(customer_json_env, monkeypatch):
    #to verify the customer balance is shown correctly
    cust = Customer()

    mock_data = {
        "id": 1111004,
        "balance": 800,
        "personal_details": {"first_name": "Meghana"}}
    
    monkeypatch.setattr(Customer, "get_details_CustomerID", lambda self : mock_data)
    assert mock_data["balance"] == 800

