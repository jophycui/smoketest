import unittest
from appium import webdriver


class TestEnv(unittest.TestCase):
    desired_caps = {'platformName': 'Android',
                    'platformVersion':'6.0.0',
                    'deviceName': '192.168.51.101:5555',
                    'appPackage': 'com.arris.workassure.ir',
                    'appActivity': '.ui.activities.LoginActivity',
                    'session-override': True}

    def setUp(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', TestEnv.desired_caps)

    def tearDown(self):
        self.driver.quit()