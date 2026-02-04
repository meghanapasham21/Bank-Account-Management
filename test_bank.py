import pytest
import customer, admin

def test_acc_type_verification():
    assert customer.Customer.acc_type_verification()