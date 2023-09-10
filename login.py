import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner
# Thêm đối tượng CustomTestResult để truyền tham chiếu
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.result = None  # Đối tượng CustomTestResult
        chrome_profile_path = "C:\\Users\\hoang\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
        options = webdriver.ChromeOptions()
        # options.add_argument(f"--user-data-dir={chrome_profile_path}")

        options = webdriver.ChromeOptions()
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable-automation"])

        self.driver = webdriver.Chrome(options=options)
    
    def test_login(self):
        self.driver.get('http://localhost:9000/login')
        username = self.driver.find_element(By.ID, value='mui-1')
        password = self.driver.find_element(By.ID, value='mui-3')
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="app_shell"]/div/div/div/div[2]/form/div[3]/button')
        username.send_keys('FM21071')
        password.send_keys('Test@123')
        submit_button.click()
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div[2]/div[1]/input'))
        )

        input_element = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[2]/div[1]/input')
        self.assertTrue(input_element.is_displayed())
        
        # Tăng giá trị success_count ở CustomTestResult
        if self.result:
            self.result.success_count += 1

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Code/FIndXTest/TestAsset/testfile'))

