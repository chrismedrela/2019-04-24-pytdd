from webtest import TestApp
from frontend import app

def before_scenario(context, scenario):
    context.client = TestApp(app)
