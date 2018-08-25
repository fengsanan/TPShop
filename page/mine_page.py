import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MinePage(BaseAction):
    login_or_sign_button = By.XPATH, "//*[@text='登录/注册']"

    @allure.step(title="点击登录/注册")
    def click_login_or_sign(self):
        self.click(self.login_or_sign_button)
        