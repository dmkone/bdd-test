from behave import *
from framework.webapp import webapp
use_step_matcher("re")


@given("I load the website")
def step_impl(context, url):
    """
    :type context: behave.runner.Context
    :type url: str
    """
    webapp.load_website()


@then("I see a page with title (?P<title>.+)")
def step_impl(context, title):
    """
    :type context: behave.runner.Context
    :type title: str
    """
    webapp.verify_title_is_displayed(title)
