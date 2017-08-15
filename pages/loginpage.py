from .base import *
from locators.loginlocators import *
from common import get_yaml


class LoginPage(BasePage):

    logininfo = get_yaml.yaml_loader("logininfo.yaml")

    def click_server_btn(self):
        element = self.driver.find_element(*LoginPageLocs.SERVER_CONF_BTN)
        element.click()

    def input_server_ip(self):
        element = self.driver.find_element(*LoginPageLocs.SERVER_IP_TB)
        element.clear()
        element.send_keys(LoginPage.logininfo['serverinfo']['ip'])

    def input_port_ip(self):
        element = self.driver.find_element(*LoginPageLocs.SERVER_PORT_TB)
        element.clear()
        element.send_keys(LoginPage.logininfo['serverinfo']['port'])

    def click_ok_btn(self):
        self.driver.find_element(*LoginPageLocs.SERVER_OK_BTN).click()

    def input_username(self):
        element = self.driver.find_element(*LoginPageLocs.USERNAME_TB)
        element.clear()
        element.send_keys(LoginPage.logininfo['login']['username'])

    def input_password(self):
        element = self.driver.find_element(*LoginPageLocs.PASSWORD_TB)
        element.clear()
        element.send_keys(LoginPage.logininfo['login']['password'])

    def click_login(self):
        pass

    def is_exist(self):
        pass