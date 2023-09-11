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
import HtmlTestRunner


class AssetList(unittest.TestCase):
    def setUp(self):

        chrome_profile_path = "C:\\Users\\hoang\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
        options = webdriver.ChromeOptions()
        options.add_argument(f"--user-data-dir={chrome_profile_path}")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        self.driver = webdriver.Chrome(options=options)
        self.current_test_steps = []

    def click_element(self, Xpath):
        div_element = self.driver.find_element(By.XPATH, Xpath)
        div_element.click()

    def test_list2(self):
        actions = ActionChains(self.driver)
        self.driver.get('http://localhost:9000/asset/list')
        try:
            WebDriverWait(self.driver, 4).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="CustomList"]'))
            )
            time.sleep(2.5)

            self.click_element(
                '//*[@id="app_shell"]/div/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div/form/div/div[2]/div[2]')
            
            # popup = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, '//html/body/div[3]/div[3]/div'))
            # )
            # time.sleep(21)
            popup_element = self.driver.find_element(By.XPATH, "//button[text()='Lưu")
            popup_element.click()
        
            # element = WebDriverWait(self.driver, 10).until(
            #     EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/div/div/div[2]/div/div[5]/span[1]/svg"))
            # )
            # element.click()
            # time.sleep(4.5)



       

            # time.sleep(20)
            # div_element = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div/form/div/div[2]/div[2')

            # for _ in range(3):
            #     actions.send_keys(Keys.ARROW_DOWN)  # Di chuyển xuống 10 lần
            # actions.send_keys(Keys.RETURN)
            # actions.perform()

            # time.sleep(1)

            # div_element.click()
            # time.sleep(0.4)
            # actions.send_keys(Keys.BACKSPACE)
            # actions.perform()

            # time.sleep(0.4)
            # click_out_side = self.driver.find_element(By.XPATH, '//*[@id="Number"]')
            # actions.click(click_out_side).perform()
            # time.sleep(0.5)

            for _ in range(344):
                actions.send_keys(Keys.ARROW_DOWN)
            actions.perform()
            # time.sleep(10)

        except NoSuchElementException:
            print('NoSuchElementException loi ')
            pdb.set_trace()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':

    unittest.main()
