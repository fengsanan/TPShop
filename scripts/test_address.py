from base.base_driver import BaseDriver
from page.page import Page


class TestAddress:
    def setup(self):
        self.driver = BaseDriver.init_driver()
        self.page = Page(self.driver)

    def test_address(self):
        self.page.home.click_mine()
        # 判断是否登录，如果没有登录，就先登录
        if not self.page.mine.is_login():
            self.page.mine.click_login_or_sign()
            self.page.login.login()
        # 查找收货地址
        if self.page.login.is_feature_exist_scroll_page(self.page.login.address_button):
            self.page.login.click_address()
            self.page.address.click_new_address()
            self.page.new_address.input_name_text("aaa")
            self.page.new_address.input_mobile_text("13800138006")
            self.page.new_address.input_address_text("5单元502")
            self.page.new_address.click_city()
            self.page.region.select_city()
            self.page.region.click_sure()
            self.page.new_address.click_save_address()
            assert self.page.address.is_toast_exist("添加成功")
        else:
            # 没定位到收货地址的话，就失败
            assert False
