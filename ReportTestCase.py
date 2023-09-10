import unittest
import time
import pdb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from page import check_for_error_script  # Đảm bảo bạn đã import module này

class Report(unittest.TestCase):
    def setUp(self):
        chrome_profile_path = "C:\\Users\\hoang\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
        options = webdriver.ChromeOptions()
        options.add_argument(f"--user-data-dir={chrome_profile_path}")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.driver = webdriver.Chrome(options=options)
        self.current_test_steps = []

        self.report_file = 'TestReport/name_report.txt'
        with open(self.report_file, 'w', encoding='utf-8') as f:
            f.write("Testcase list step Report\n")

    def log_error_and_steps(self, error_message):
        self.current_test_steps.append("Error appeared: " + error_message)
        with open(self.report_file, 'a', encoding='utf-8') as f:
            for step in self.current_test_steps:
                f.write(f"  - {step}\n")
        pdb.set_trace()
        # check_for_error_script(self.driver)

    def test_list(self):
        self.driver.get('http://localhost:9000/asset/lists')
        time.sleep(1)

        try:
            self.current_test_steps.append("Step 1: Thực hiện bước 1")
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="CustomList"]'))
            )
            self.current_test_steps.append("Step 2: Thực hiện bước 2")

        except (NoSuchElementException, TimeoutException) as e:
            self.log_error_and_steps(str(e))
        except Exception as e:
            self.log_error_and_steps(str(e))

    def tearDown(self):
        with open(self.report_file, 'a', encoding='utf-8') as f:
            for step in self.current_test_steps:
                f.write(f"  - {step}\n")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
