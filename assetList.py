import unittest
import time
import pdb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from page import check_for_error_script
import HtmlTestRunner
class AssetList(unittest.TestCase):
    def setUp(self):
        self.report_file = 'TestReport/AssetList_report.txt'

        chrome_profile_path = "C:\\Users\\hoang\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
        options = webdriver.ChromeOptions()
        options.add_argument(f"--user-data-dir={chrome_profile_path}")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.driver = webdriver.Chrome(options=options)
        self.current_test_steps = []

        with open(self.report_file, 'w', encoding='utf-8') as f:
            f.write("Testcase list step Report\n")

    def log_error_and_steps(self, error_message):
        self.current_test_steps.append("Error appeared: " + error_message)
        with open(self.report_file, 'a', encoding='utf-8') as f:
            for step in self.current_test_steps:
                f.write(f"  - {step}\n")
        pdb.set_trace()

    def test_list(self):
        actions = ActionChains(self.driver)

        self.driver.get('http://localhost:9000/asset/list')
        time.sleep(1.5)

        try:
            self.current_test_steps.append("Step 1: Thực hiện bước 1")
            self.current_test_steps.append("Step 2: Thực hiện bước 2")

            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="CustomList"]'))
            )

            div_element = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div/form/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]')
            div_element.click()
            time.sleep(0.5)
            
            for _ in range(3):
                actions.send_keys(Keys.ARROW_DOWN)  # Di chuyển xuống 10 lần
            actions.send_keys(Keys.RETURN)
            actions.perform()

            time.sleep(1)

            div_element.click()
            time.sleep(0.4)
            actions.send_keys(Keys.BACKSPACE)
            actions.perform()

            time.sleep(0.4)
            click_out_side = self.driver.find_element(By.XPATH, '//*[@id="Number"]')
            actions.click(click_out_side).perform()
            time.sleep(0.5)

            for _ in range(344):
                actions.send_keys(Keys.ARROW_DOWN) 
            actions.perform()
            # time.sleep(10)

        except NoSuchElementException:
            print('NoSuchElementException loi ')
            pdb.set_trace()
            check_for_error_script(self.driver)
    def test_list2(self):
        actions = ActionChains(self.driver)

        self.driver.get('http://localhost:9000/asset/list')
        time.sleep(1.5)

        try:
            self.current_test_steps.append("Step 1: Thực hiện bước 1")
            self.current_test_steps.append("Step 2: Thực hiện bước 2")

            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="CustomListssss"]'))
            )

            div_element = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div/form/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[1]')
            div_element.click()
            time.sleep(0.5)
            
            
            for _ in range(3):
                actions.send_keys(Keys.ARROW_DOWN)  # Di chuyển xuống 10 lần
            actions.send_keys(Keys.RETURN)
            actions.perform()

            time.sleep(1)

            div_element.click()
            time.sleep(0.4)
            actions.send_keys(Keys.BACKSPACE)
            actions.perform()

            time.sleep(0.4)
            click_out_side = self.driver.find_element(By.XPATH, '//*[@id="Number"]')
            actions.click(click_out_side).perform()
            time.sleep(0.5)

            for _ in range(344):
                actions.send_keys(Keys.ARROW_DOWN) 
            actions.perform()
            # time.sleep(10)

        except NoSuchElementException:
            print('NoSuchElementException loi ')
            pdb.set_trace()
            check_for_error_script(self.driver)

    def tearDown(self):
        with open(self.report_file, 'a', encoding='utf-8') as f:
            for step in self.current_test_steps:
                f.write(f"  - {step}\n")
        self.driver.quit()
