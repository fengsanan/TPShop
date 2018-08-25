import random
import time

import allure
import pytest
from allure.constants import AttachmentType
from selenium.webdriver.common.by import By

from base.base_analyze import analyze_with_file
from base.base_driver import BaseDriver
from page.page import Page


def random_password():
    password = ""
    for i in range(9):
        password += str(random.randint(0, 9))
    return password


def show_password_num():
    password_list = list()
    for i in range(2):
        password_list.append(random_password())
    return password_list


class TestLogin:
    def setup(self):
        self.driver = BaseDriver.init_driver()
        # self.base_action = BaseAction(self.driver)
        self.page = Page(self.driver)

    # def test_toase(self):
    #     self.base_action.press_back()
    #     time.sleep(2)
    #     self.base_action.press_back()
    #     time.sleep(2)
    #     print(self.base_action.find_toast(self.driver, "可退出"))
    # @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login"))
    # def test_login(self, args):
    #     username = args["username"]
    #     password = args["password"]
    #     expect = args["expect"]
    #     self.page.home.click_mine()
    #     self.page.mine.click_login_or_sign()
    #     self.page.login.input_username(username)
    #     self.page.login.input_password(password)
    #     self.page.login.click_login()
    #     assert self.page.login.is_toast_exist(expect)
    #
    @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login_miss_part"))
    def test_login_miss_part(self, args):
        username = args["username"]
        password = args["password"]
        self.page.home.click_mine()
        self.page.mine.click_login_or_sign()
        self.page.login.input_username(username)
        self.page.login.input_password(password)
        time.sleep(2)
        assert not self.page.login.is_login_button_enabled()

    @pytest.mark.parametrize("password", show_password_num())
    def test_show_password(self, password):
        password_element = By.XPATH, "//*[@text='" + password + "']"

        self.page.home.click_mine()
        self.page.mine.click_login_or_sign()
        self.page.login.input_password(password)
        time.sleep(2)
        assert not self.page.login.is_feature_exist(password_element)
        self.page.login.click_show_password()
        time.sleep(2)
        allure.attach("显示密码",self.driver.get_screenshot_as_png(),AttachmentType.PNG)
        assert self.page.login.is_feature_exist(password_element)
