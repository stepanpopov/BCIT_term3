import pytest
from pytest_bdd import scenario, given, when, then
from sort import sort1

@scenario('feauture.feauture','Sort_abs')
def test_sort_abs1():
    print('End of test sort_abs1')
    pass

@given('There is an array which is [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]')
def list():
    list = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
    return list

@when('I sort1 this array')
def sorted_list(list):
    begin_list = sort1(list)
    

@then('Array is [123, 100, -100, -30, 30, 4, -4, 1, -1, 0]')
def final_list(list):
    assert list == [123, 100, -100, -30, 30, 4, -4, 1, -1, 0]
