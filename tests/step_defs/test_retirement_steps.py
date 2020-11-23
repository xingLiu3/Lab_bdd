from pytest_bdd import scenarios, parsers, given, when, then

from retirement import *


EXTRA_TYPES = {
    'Number': int,
}


CONVERTERS = {
    'birthyear': int,
    'age': int,
    'month': int,
    'birthmonth': int,
    'ageyear': int,
    'agemonth': int,
    'year': int,
}


scenarios('../features/cucumbers.feature', example_converters=CONVERTERS)

@given(parsers.cfparse('the retirement age is initialed', extra_types=EXTRA_TYPES), target_fixture='retireage')
@given('the retirement age is initialed', target_fixture='retireage')
def retireage():
    return RetireAge()

@when(parsers.cfparse('"{birthyear:Number}" is entered', extra_types=EXTRA_TYPES))
@when('"<birthyear>" is entered')
def test_calculate_retirement_age(retireage, birthyear):
    retireage.calculate_retirement_age(birthyear)

@then(parsers.cfparse('the result is "{age:Number}", "{month:Number}"', extra_types=EXTRA_TYPES))
@then('the result is "<age>", "<month>"')
def test_retirement_age(retireage, age, month):
    assert retireage._age == age
    assert retireage._month == month

@given(parsers.cfparse('the retirement date is initialed', extra_types=EXTRA_TYPES), target_fixture='retiredate')
@given('the retirement date is initialed', target_fixture='retiredate')
def retiredate():
    return RetireDate()

@when(parsers.cfparse('"{birthyear:Number}", "{birthmonth:Number}", "{ageyear:Number}", "{agemonth:Number}" is entered', extra_types=EXTRA_TYPES))
@when('"<birthyear>", "<birthmonth>", "<ageyear>", "<agemonth>" is entered')
def calculate_retirement_date(retiredate, birthyear, birthmonth, ageyear, agemonth):
    retiredate.calculate_retirement_date(birthyear, birthmonth, ageyear, agemonth)

@then(parsers.cfparse('the result is "{year:Number}", "{month:Number}"', extra_types=EXTRA_TYPES))
@then('the result is "<year>", "<month>"')
def test_retirement_date(retirdate, year, month):
    assert retiredate._year == year
    assert retiredate._month == month
