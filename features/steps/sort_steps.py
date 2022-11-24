from behave import given, when, then, step
from lab_python_fp.sort import sort1

@given("There is an array which is [{array}]")
def step_have_array(context, array):
    context.array = [int(i) for i in list(array.split(', '))]

@when("I sort1 this array")
def step_sort1_array(context):
    context.sorted_array = sort1(context.array)

@then("Array is [{array}]")
def step_expect_result(context, array):
    result = [int(i) for i in list(array.split(', '))]
    assert context.sorted_array == result
