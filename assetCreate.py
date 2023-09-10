import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import HtmlTestRunner
import pdb; 

class AssetCreate(unittest.TestCase):
    def setUp(self):
        self.report_file = 'TestReport/AssetCreate_report.txt'


        chrome_profile_path = "C:\\Users\\hoang\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
        options = webdriver.ChromeOptions()
        options.add_argument(f"--user-data-dir={chrome_profile_path}")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.driver = webdriver.Chrome(options=options)
        self.current_test_steps = []

        with open(self.report_file, 'w', encoding='utf-8') as f:
            f.write("Testcase list step Report\n")

    def test_create(self):
        self.driver.get('http://localhost:9000/asset/create')

        try:
            self.current_test_steps.append("Step 1: Thực hiện bước 1")
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'Name'))
            )

            nameAsset = self.driver.find_element(By.NAME, 'Name')
            codeAsset = self.driver.find_element(By.NAME, 'Code')
            submit = self.driver.find_element(By.XPATH, '//*[@id="mui-5"]')

            nameAsset.send_keys('FM21071')
            codeAsset.send_keys('Test@123')

            self.driver.find_element(By.ID, 'react-select-2-input').click();
            time.sleep(0.6)
            actions = ActionChains(self.driver)
            for _ in range(10):
                actions.send_keys(Keys.ARROW_DOWN)  # Di chuyển xuống 10 lần
            actions.send_keys(Keys.RETURN)  # Chọn tùy chọn bằng cách nhấn Enter
            actions.perform()

            
            submit.click()
            div_element =self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/form/div[1]/div[6]')
            
            actions.move_to_element(div_element).perform()
            self.current_test_steps.append("Step 2: Thực hiện bước 2")

        except (NoSuchElementException, TimeoutException) as e:
            self.log_error_and_steps(str(e))
        except Exception as e:
            self.log_error_and_steps(str(e))    

        # pdb.set_trace()
    def tearDown(self):
        with open(self.report_file, 'a', encoding='utf-8') as f:
            for step in self.current_test_steps:
                f.write(f"  - {step}\n")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Code/FIndXTest/TestAsset/testfile'))

