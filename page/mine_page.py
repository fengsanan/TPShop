import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MinePage(BaseAction):
    login_or_sign_button = By.XPATH, "//*[@text='登录/注册']"
    setting_button = By.ID, "com.tpshop.malls:id/setting_btn"
    title_text = By.ID, "com.tpshop.malls:id/titlebar_title_txtv"

    @allure.step(title="点击登录/注册")
    def click_login_or_sign(self):
        self.click(self.login_or_sign_button)

    @allure.step(title="点击设置")
    def click_setting(self):
        self.click(self.setting_button)

    def is_login(self):
        self.click_setting()
        is_login = not self.find_element(self.title_text).text == "登录"
        self.press_back()
        return is_login
