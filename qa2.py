from selenium import webdriver
from selenium.webdriver.common.by import By


class Test1:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_1(self):
        self.driver.get("https://qa2-pmteam.xyz/uk")
        self.driver.set_window_size(1920, 1040)
        self.driver.implicitly_wait(100)
        self.driver.find_element(By.CSS_SELECTOR, ".userinfo__signIn > .button__content").click()
        self.driver.find_element(By.NAME, "login").click()
        self.driver.find_element(By.NAME, "login").send_keys("chistyakov")
        self.driver.find_element(By.NAME, "password").send_keys("Fyukbz8087702")
        self.driver.find_element(By.CSS_SELECTOR, ".input__icon_eye").click()
        self.driver.find_element(By.CSS_SELECTOR, ".button_size_m").click()
        self.driver.find_element(By.CSS_SELECTOR, ".header__menuBtn").click()
        self.driver.get("https://qa2-pmteam.xyz/api/v2/logout")
        print("All done")
