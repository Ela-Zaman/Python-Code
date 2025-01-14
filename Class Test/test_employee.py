import pytest
from employee import Employee

@pytest.fixture
def employee():
    employee = Employee("Razia Zaman","Ela",10000)
    return employee

def test_give_default_raise(employee):
    annual_salary = employee.give_raise()

    assert annual_salary == 15000

def test_give_custom_raise(employee):
    annual_salary = employee.give_raise(10000)

    assert annual_salary == 20000