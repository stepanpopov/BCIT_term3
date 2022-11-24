from behave import given, when, then
from lab_python_fp.sort import sort1, sort2

@given("There is an array which is [{array}]")
def step_have_array(context, array):
    context.array = [int(i) for i in array.split(', ')]

@when("I sort this array originally")
def step_sort1_array(context):
    context.sorted_array = sort1(context.array)

@when("I sort this array with lambda")
def step_sort1_array(context):
    context.sorted_array = sort2(context.array)

@then("Array is [{array}]")
def step_expect_result(context, array):
    result = [int(i) for i in array.split(', ')]
    assert context.sorted_array == result
