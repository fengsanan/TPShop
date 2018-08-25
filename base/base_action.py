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

    def click(self, feature, timeout=10, poll=1):
        self.find_element(feature).click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

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
