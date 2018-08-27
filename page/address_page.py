import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressPage(BaseAction):
    new_address_button = By.ID, "com.tpshop.malls:id/add_address_btn"

    @allure.step(title="点击新建地址")
    def click_new_address(self):
        self.click(self.new_address_button)
