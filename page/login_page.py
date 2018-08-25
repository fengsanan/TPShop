import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username_text = By.ID, "com.tpshop.malls:id/edit_phone_num"
    password_text = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"
    show_password_button = By.ID,"com.tpshop.malls:id/img_view_pwd"

    @allure.step(title="输入用户名")
    def input_username(self, text):
        allure.attach("用户名："+text,"")
        self.input(self.username_text, text)

    @allure.step(title="输入密码")
    def input_password(self, text):
        allure.attach("密码：" + text, "")
        self.input(self.password_text, text)

    @allure.step(title="点击登录")
    def click_login(self):
        self.click(self.login_button)

    @allure.step(title="点击显示密码")
    def click_show_password(self):
        self.click(self.show_password_button)

    def is_login_button_enabled(self):
        return self.is_feature_enabled(self.login_button)



