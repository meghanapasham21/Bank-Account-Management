import json
import pytest
from customer import Customer
from admin import Admin
from unittest.mock import MagicMock, patch

def test_json_file_exists(monkeypatch, tmp_path):
    
    #create a fake json file
    cust_data = [{'id': 200, 'name': 'Meghana'}]
    json_file = tmp_path/'cust_data.json'
    json_file.write_text(json.dumps(cust_data))

    monkeypatch.chdir(json_file)
    Cust = Customer()

    assert Cust.jsonData == cust_data
    assert Cust.customer_id == 200


