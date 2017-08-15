from common import test_env
from pages.loginpage import *
import unittest


class Login(test_env.TestEnv):
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.click_server_btn()
        login_page.input_server_ip()
        login_page.input_port_ip()
        login_page.click_ok_btn()
        login_page.input_username()
        login_page.input_password()


if __name__ == "__main__":
    unittest.main(verbosity=2)