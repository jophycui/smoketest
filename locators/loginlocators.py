from selenium.webdriver.common.by import By


class LoginPageLocs(object):
    SERVER_CONF_BTN = (By.ID, 'com.arris.workassure.ir:id/server_ip')
    SERVER_IP_TB = (By.ID, 'com.arris.workassure.ir:id/server')
    SERVER_PORT_TB = (By.ID, 'com.arris.workassure.ir:id/port')
    SERVER_OK_BTN = (By.ID, 'com.arris.workassure.ir:id/change')

    USERNAME_TB = (By.ID, 'com.arris.workassure.ir:id/user_id')
    PASSWORD_TB = (By.ID, 'com.arris.workassure.ir:id/password')

