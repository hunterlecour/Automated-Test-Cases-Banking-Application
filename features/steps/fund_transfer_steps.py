from behave import given, when, then


@when('Click Fund Transfer')
def click_fund_transfer(context):
    context.app.fund_transfer_page.click_fund_transfer()


@when('Input Correct Required Fields For Fund Transfer')
def correct_required_fields(context):
    context.app.fund_transfer_page.correct_required_fields()


@when('Click Submit')
def click_submit(context):
    context.app.fund_transfer_page.click_submit()


@when('Input Incorrect Required Fields For Fund Transfer')
def incorrect_required_fields(context):
    context.app.fund_transfer_page.incorrect_required_fields()


@then('Verify Fund Transfer Successful')
def verify_fund_transfer(context):
    context.app.fund_transfer_page.verify_fund_transfer()


@then('Verify Page Is Redirecting To Fund Transfer Page')
def verify_transfer_page(context):
    context.app.fund_transfer_page.verify_transfer_page()


@then('Verify A Pop - UP {pop_up} is visible')
def verify_account_doesnt_exist(context, pop_up):
    context.app.fund_transfer_page.verify_account_doesnt_exist(pop_up)




