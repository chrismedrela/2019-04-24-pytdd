from webtest import TestApp

import webapp


def before_scenario(context, scenario):
    context.client = TestApp(webapp.app)


def after_scenario(context, scenario):
    del context.client
