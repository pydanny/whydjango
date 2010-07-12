"""
    Taken from Alex Gaynor's test utilities::
    
        http://alexgaynor.net/2010/jul/06/testing-utilities-django/
"""

from django.test import TestCase 
from django.contrib.auth.models import User 

class TestTests(TestCase): 
    def test_environment(self):
        """ Test that tests can run """ 
        self.assert_(True)
        
class login(object):
    def __init__(self, testcase, user, password):
        self.testcase = testcase
        success = testcase.client.login(username=user, password=password)
        self.testcase.assertTrue(
            success,
            "login with username=%r, password=%r failed" % (user, password)
        )

    def __enter__(self):
        pass

    def __exit__(self, *args):
        self.testcase.client.logout()

class BaseTestCase(TestCase):
    """
    Setup default StoryMarket test case
    """

    fixtures = ['testauthdata', 'initial_metrics']
    urls = 'storymarket.urls'

    def setUp(self):
        u = User.objects.get(username='testclient')
        self.client.login(username='testclient', password='password')

    def tearDown(self):
        self.client.logout()
        
    def login(self, user, password):
        return login(self, user, password)        
        
    def get(self, url_name, *args, **kwargs):
        return self.client.get(reverse(url_name, args=args, kwargs=kwargs))

    def post(self, url_name, *args, **kwargs):
        data = kwargs.pop("data", None)
        return self.client.post(reverse(url_name, args=arg