from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username_text = By.ID, "com.tpshop.malls:id/edit_phone_num"
    password_text = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    def input_username(self, text):
        self.input(self.username_text, text)

    def input_password(self, text):
        self.input(self.password_text, text)

    def click_login(self):
        self.click(self.login_button)

    def is_login_button_enabled(self):
        if self.find_element(self.login_button).get_attribute("enabled") == "ture":
            return True
        return False
