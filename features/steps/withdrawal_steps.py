from behave import given, when, then


@when('Click Withdrawal')
def withdrawal_button(context):
    context.app.withdrawal_page.withdrawal_button()
    # THIS IS FAILING


@when('Enter Account No {account_number_input}')
def account_number(context, account_number_input):
    context.app.withdrawal_page.account_number(account_number_input)


@when('Enter Amount {amount} dollars')
def amount_number(context, amount):
    context.app.withdrawal_page.amount_number(amount)


@when('Enter Description {input}')
def withdrawal_desc(context, input):
    context.app.withdrawal_page.withdrawal_desc(input)


@then('Verify Withdrawal Is Successful')
def verify_withdrawal(context):
    context.app.withdrawal_page.verify_withdrawal()







