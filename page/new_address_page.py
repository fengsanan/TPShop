import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewAddressPage(BaseAction):
    name_text = By.ID, "com.tpshop.malls:id/consignee_name_edtv"
    mobile_text = By.ID, "com.tpshop.malls:id/consignee_mobile_edtv"
    address_text = By.ID, "com.tpshop.malls:id/consignee_address_edtv"
    save_address_button = By.ID, "com.tpshop.malls:id/submit_btn"
    city_button = By.ID, "com.tpshop.malls:id/consignee_region_txtv"

    @allure.step(title="输入收货人")
    def input_name_text(self, text):
        self.input(self.name_text, text)

    @allure.step(title="输入收货人手机号")
    def input_mobile_text(self, text):
        self.input(self.mobile_text, text)

    @allure.step(title="输入详细地址")
    def input_address_text(self, text):
        self.input(self.address_text, text)

    @allure.step(title="点击保存地址")
    def click_save_address(self):
        self.click(self.save_address_button)

    @allure.step(title="点击选择区域")
    def click_city(self):
        print("点击选择区域")
        self.click(self.city_button)
