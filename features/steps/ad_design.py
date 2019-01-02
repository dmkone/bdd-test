from behave import *
use_step_matcher("re")


@step("At least one ad design is created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_ad_design_page_is_not_empty()


@when("I hover over the ad design")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.hover_over_ad_design_block()


@then("I should see 5 action icons")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.adsdesignpage.verify_action_icons_visible()
