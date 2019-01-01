from behave import *
from features.pages.login_page import LoginPage
from features.pages.ad_design import AdDesignPage
from webdriver import Driver

use_step_matcher("re")


@given("I am logged in")
def step_impl_validate_logged_in(context):
    """
    :type context: behave.runner.Context
    """
    driver = Driver()
    loginpage = LoginPage(driver)
    driver = loginpage.log_in()
    context.adsdesignpage = AdDesignPage(driver)


@when('I click on "Ad Designs" tab')
def step_impl_click(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.click_menu()


@then("I should see Ad Design page")
def step_impl_validate_page_is_opened(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_on_ad_design_page()
    context.adsdesignpage.close_website()


@given("I am on Ad Design page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = Driver()
    loginpage = LoginPage(driver)
    driver = loginpage.log_in()
    context.adsdesignpage = AdDesignPage(driver)
    context.adsdesignpage.click_menu()
    context.adsdesignpage.verify_on_ad_design_page()


@when('I click on "Create Ad Design" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.click_create_ad_design_button()


@then("I should see a popup for Ad Design creation")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_design_popup_is_displayed()
    context.adsdesignpage.close_website()


@when("I select (?P<ad_account>.+) Ad Account from drop-down")
def step_impl(context, ad_account):
    """
    :type ad_account: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.pick_ad_account(ad_account)


@then("That ad account is the selected option")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I select (?P<page>.+) Page from Pages drop-down")
def step_impl(context, page):
    """
    :type page: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.select_page(page)


@then("That page is the selected option")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I click on Pages drop-down")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.click_on_pages()


@then("I enter 3 letters in the page input box")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.fill_in_letters()


@step("I should see matching pages automatically filtered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.filter_pages()


@when("I select an (?P<ad_type>.+) from Ad types drop-down")
def step_impl(context, ad_type):
    """
    :type ad_type: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.select_ad_type(ad_type)


@then("I should see all the ad designs of (?P<ad_type>.+) ad type")
def step_impl(context, ad_type):
    """
    :type ad_type: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.display_filtered_ad_designs(ad_type)


@when("I select a date (?P<date>.+) from Date picker drop-down")
def step_impl(context, date):
    """
    :type context: behave.runner.Context
    :type date: str
    """
    context.adsdesignpage.select_date_range(date)


@when("I enter an existing tag in Tags input field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.enter_tag()


@when("I click on Instagram icon")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.click_instagram_icon()


@step("The page contains ad designs of all 6 objectives")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I can see thumbnail images for all the ad designs")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_design_images_displayed()


@step("At least two of any type of ad designs are created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I select Date - Oldest to Newest")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.select_date_from_dropdown()


@then("The ad designs are sorted from oldest to newest")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.newest_to_oldest()


@step("I should see ad designs belonging to that account")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.adaccount_ad_desings()


@step("I should see ad designs with pageid (?P<page_id>.+)")
def step_impl(context, page_id):
    """
    :type page_id: str
    :type context: behave.runner.Context
    """
    context.adsdesignpage.page_ad_desings(page_id)