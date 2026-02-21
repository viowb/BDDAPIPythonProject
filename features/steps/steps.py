from behave import given, when, then

@given("I have a clean environment")
def step_impl(context):
    # setup steps
    pass

@when("I run behave")
def step_impl(context):
    # action steps
    pass

@then("it should not crash")
def step_impl(context):
    # verification steps
    pass
