from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10.0, poll=1.0):
        by, value = feature
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_element(by, value))

    def find_elements(self, feature, timeout=10.0, poll=1.0):
        by, value = feature
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_elements(by, value))

    def click(self, feature, timeout=10.0, poll=1.0):
        self.find_element(feature).click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    def press_keycode(self):
        pass

    def press_back(self):
        self.driver.press_keycode(4)

    def press_enter(self):
        self.driver.press_keycode(66)

    def find_toast(self, message, timeout=3):
        """
        # message: 预期要获取的toast的部分消息
        """
        message = By.XPATH, "//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位

        element = self.find_element(message, timeout, 0.1)
        return element.text

    def is_toast_exist(self, message):
        try:
            self.find_toast(message)
            return True
        except Exception:
            return False

    # 判断元素是否可用
    def is_feature_enabled(self, feature):
        return self.find_element(feature).get_attribute("enabled") == "ture"

    # 判断元素是否可点击
    def is_feature_clickable(self, feature):
        return self.find_element(feature).get_attribute("clickable") == "ture"

    # 判断元素是可能够找到
    def is_feature_exist(self, feature):
        try:
            self.find_element(feature)
            return True
        except Exception:
            return False

    def scroll_page_one_time(self, direction="up"):
        size = self.driver.get_window_size()
        size_width = size["width"]
        size_height = size["height"]
        center_x = size_width * 0.5
        center_y = size_height * 0.5

        top_x = center_x
        top_y = center_y * 0.25
        down_x = center_x
        down_y = center_y * 0.75
        left_x = center_x * 0.25
        left_y = center_y
        right_x = center_x * 0.75
        right_y = center_y

        if direction == "up":
            self.driver.swipe(down_x, down_y, top_x, top_y,2000)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, down_x, down_y,2000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y,2000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y,2000)
        else:
            raise Exception("请输入up、down、left、right")

    def is_feature_exist_scroll_page(self, feature, direction="up"):
        old_page_source = None
        new_page_source = self.driver.page_source
        while True:
            print("定位收货地址")
            if self.is_feature_exist(feature):
                print("定位到了收货地址")
                return True
            else:
                print("判断是否到最后一页")
                if not new_page_source == old_page_source:
                    print("翻页")
                    self.scroll_page_one_time(direction)
                    old_page_source = new_page_source
                    new_page_source = self.driver.page_source
                else:
                    return False
