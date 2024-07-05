from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open soft.reelly page')
def open_soft_reelly(context):
    context.app.main_page.open_main()
    sleep(5)


@when('Input name field')
def input_fields(context):
    context.app.login_page.input_fields()


@then('Input phone field')
def input_fields_phone(context):
    context.app.login_page.input_fields_phone()


@then('Input pwd field')
def input_fields_pwd(context):
    context.app.login_page.input_fields_pwd()


@then('Input comp_web field')
def input_fields_comp_web(context):
    context.app.login_page.input_fields_comp_web()


@then('Choose role field')
def dropdown_menu_role(context):
    context.app.login_page.dropdown_menu_role()


@then('Choose country field')
def dropdown_menu_country(context):
    context.app.login_page.dropdown_menu_country()


@then('Choose comp_size field')
def dropdown_menu_comp_size(context):
    context.app.login_page.dropdown_menu_comp_size()


@then('Press_on_the_button')
def click_create_account(context):
    context.app.login_page.click_create_account()


@then('Verify expected URL')
def verify_page(context):
    context.app.login_page.verify_page('https://soft.reelly.io/sign-up')


@then('Verify_the_button')
def verify_the_button(context):
    context.app.login_page.verify_the_button()
#
# @given('Login to the page')
# def input_credentials(context):
#     context.app.login_page.input_credentials()
#
#
# @given('Click on continue button')
# def click_search_icon(context):
#     context.app.login_page.click_sign_in()
#
#
# @given('Click on settings open')
# def click_on_settings(context):
#     context.app.login_page.click_on_settings()
#
#
# @given('Click on Edit profile option')
# def edit_profile(context):
#     context.app.login_page.edit_profile()
#
#
# @given('Enter some test information in the input fields')
# def input_fields(context):
#     context.app.login_page.input_fields()
#     sleep(3)
#
#
# @given('Check the right information is present in the input fields')
# def verify_input_fields(context):
#     context.app.login_page.verify_input_fields()
#
#
# @given('Click on Save changes')
# def click_on_save(context):
#     context.app.login_page.click_save_changes()
#
#
# @given('Click on Close')
# def click_on_close(context):
#     context.app.login_page.click_on_close()

# def verify_found_results_text(context, search_word):
#     assert search_word.lower() in context.driver.current_url.lower(), \
#         f'Expected query not in {context.driver.current_url.lower()}'
