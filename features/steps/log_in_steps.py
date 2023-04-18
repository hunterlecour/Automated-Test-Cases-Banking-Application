from behave import given, when, then


@given('Open Bank App')
def open_bank_app(context):
    context.app.login_page.open_bank_app()


@when('Enter Valid User ID {login_input}')
def login(context, login_input):
    context.app.login_page.login(login_input)


@when('Enter Invalid User ID {invalid_login_input}')
def login_id_wrong(context, invalid_login_input):
    context.app.login_page.login_id_wrong(invalid_login_input)


@when('Enter Valid Password {password_input}')
def password(context, password_input):
    context.app.login_page.password(password_input)


@when('Enter Invalid Password {invalid_password_input}')
def password_wrong(context, invalid_password_input):
    context.app.login_page.password_wrong(invalid_password_input)


@when('Click Login')
def login_click(context):
    context.app.login_page.login_click()


@when('Click Logout')
def logout_click(context):
    context.app.login_page.logout_click()


@then('Verify Login Is Successful')
def verify_login(context):
    context.app.login_page.verify_login()


@then('Verify Login is Unsuccessful')
def verify_login_error(context):
    context.app.login_page.verify_login_error()


@then('Verify User Can Log Out')
def verify_logout(context):
    context.app.login_page.verify_logout()



