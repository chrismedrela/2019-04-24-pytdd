from behave import *

@step('a user navigates to home page')
def step_impl(context):
    context.resp = context.client.get('/')

@then('{text} should be displayed')
def step_impl(context, text):
    assert text in context.resp

@given('I have entered {value} as {field_name} number')
def step_impl(context, value, field_name):
    context.resp.form[field_name] = value

@when('I press add')
def step_impl(context):
    context.resp = context.resp.form.submit()
