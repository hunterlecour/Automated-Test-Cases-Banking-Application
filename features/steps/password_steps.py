from behave import given, when, then


@when('Click Change Password')
def click_change_password(context):
    context.app.password_page.click_change_password()


@when('Enter Incorrect Old Password {incorrect_input}')
def incorrect_old_password(context, incorrect_input):
    context.app.password_page.incorrect_old_password(incorrect_input)


@when('Enter New Password Credentials {new_password_input}')
def new_password_credential(context, new_password_input):
    context.app.password_page.new_password_credential(new_password_input)


@then('Verify User Is Unable to Change Password')
def verify_password_error(context):
    context.app.password_page.verify_password_error()







