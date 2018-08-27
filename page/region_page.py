import random
import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class RegionPage(BaseAction):
    city = By.ID, "com.tpshop.malls:id/tv_city"
    sure_button = By.ID, "com.tpshop.malls:id/btn_right"

    def select_city(self):
        print("选择城市")

        for i in range(4):
            print("获取城市列表，循环4次")
            cities = self.find_elements(self.city)
            print("随机一个数字做为下标")
            city_index = random.randint(0, len(cities) - 1)
            print("点击这个无素")
            cities[city_index].click()
            time.sleep(2)

    def click_sure(self):
        self.click(self.sure_button)
