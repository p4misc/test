import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class TestGoogle:

    driver = webdriver.Chrome(ChromeDriverManager().install())

    def setup_class(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        climport pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class TestGoogle:

    driver = webdriver.Chrome(ChromeDriverManager().install())

    def setup_class(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()

    def setup_method(self):
        self.driver.get("https://google.com")

    def test_case(self):
        driver = self.driver

        #driver.save_screenshot("test-reports/result_001.png")

        #driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input").send_keys("hoge")

        #driver.save_screenshot("test-reports/result_002.png")

        #driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div > div.FPdoLc.VlcLAe > center > input.gNO89b").click()

        #driver.save_screenshot("test-reports/result_003.png")

        assert driver.title.count('hoge'), "ページタイトルにhogeが含まれていること"

    def teardown_class(cls):
        cls.driver.quit()
s.driver.maximize_window()

    def setup_method(self):
        self.driver.get("https://google.com")

    def test_case(self):
        driver = self.driver

        driver.save_screenshot("test-reports/result_001.png")

        driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input").send_keys("hoge")

        driver.save_screenshot("test-reports/result_002.png")

        driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div > div.FPdoLc.VlcLAe > center > input.gNO89b").click()

        driver.save_screenshot("test-reports/result_003.png")

        assert driver.title.count('hoge'), "繝壹�ｼ繧ｸ繧ｿ繧､繝医Ν縺ｫhoge縺悟性縺ｾ繧後※縺�繧九％縺ｨ"

    def teardown_class(cls):
        cls.driver.quit()
