from framework.webapp import webapp


def before_all(context):
    context.webapp = webapp

def after_all(context):
    context.webapp.close_website()
