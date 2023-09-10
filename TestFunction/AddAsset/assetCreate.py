import getpass
import unittest
import json
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner

class AssetCreatePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_asset_details(self, name, text):
        name_asset = self.driver.find_element(By.NAME, name)
        name_asset.send_keys(text)

    def select_option(self, select_box_id, option_index):
        select_element = self.driver.find_element(By.ID, select_box_id)
        select_element.click()
        
        for _ in range(option_index - 1):
            select_element.send_keys(Keys.ARROW_DOWN)
        
        select_element.send_keys(Keys.RETURN)

    def submit_form(self):
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="mui-5"]')
        submit_button.click()

class AssetCreate(unittest.TestCase):
    def setUp(self):
        self.test_data = self.read_test_data('C:/Code/FIndXTest/TestAsset/TestFunction/AddAsset/test_data.json')
        chrome_profile_path = "C:\\Users\\hoang\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
        options = webdriver.ChromeOptions()
        options.add_argument(f"--user-data-dir={chrome_profile_path}")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.driver = webdriver.Chrome(options=options)
        self.asset_create_page = AssetCreatePage(self.driver)
       
    def read_test_data(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def create_asset(self, asset_data):
        self.driver.get("https://ilove.fmplustest.xyz/asset/create")

        characters = string.ascii_letters + string.digits
        random_code = ''.join(random.choice(characters) for _ in range(5))
        self.asset_create_page.enter_asset_details('Name', asset_data['name'])
        self.asset_create_page.enter_asset_details('Code', random_code)
        self.asset_create_page.select_option('react-select-2-input', asset_data['TypeId'])
        self.asset_create_page.select_option('react-select-3-input', asset_data['GroupId'])
        self.asset_create_page.select_option('react-select-4-input', asset_data['Category'])
        self.asset_create_page.select_option('react-select-5-input', asset_data['StatusQuality'])
        self.asset_create_page.select_option('react-select-6-input', asset_data['StatusBuy'])
        self.asset_create_page.select_option('react-select-7-input', asset_data['UnitId'])
        self.asset_create_page.enter_asset_details('Quantity', asset_data['Quantity'])
        self.asset_create_page.enter_asset_details('PurchasePrice', asset_data['PurchasePrice'])
        self.asset_create_page.select_option('react-select-8-input', asset_data['VendorId'])
        self.asset_create_page.select_option('react-select-9-input', asset_data['UserId'])
        self.asset_create_page.enter_asset_details('ManufacturerCode', asset_data['ManufacturerCode'])
        self.asset_create_page.enter_asset_details('Serial', asset_data['Serial'])
        self.asset_create_page.enter_asset_details('ManufactureYear', asset_data['ManufactureYear'])
        self.asset_create_page.enter_asset_details('Country', asset_data['Country'])
        self.asset_create_page.enter_asset_details('GuaranteeTime', asset_data['GuaranteeTime'])
        self.asset_create_page.enter_asset_details('ConditionApplyGuarantee', asset_data['ConditionApplyGuarantee'])
        self.asset_create_page.enter_asset_details('OriginalPrice', asset_data['OriginalPrice'])
        self.asset_create_page.enter_asset_details('DepreciatedValue', asset_data['DepreciatedValue'])
        self.asset_create_page.enter_asset_details('DepreciatedMonth', asset_data['DepreciatedMonth'])
        self.asset_create_page.submit_form()
       
        WebDriverWait(self.driver, 6).until(
            EC.presence_of_element_located((By.ID, 'CustomList'))
        )

        self.driver.find_element(By.ID, 'CustomList')


    def test_create_with_test_data_1(self):
        self.create_asset(self.test_data["1"])

    def test_create_with_test_data_2(self):
        self.create_asset(self.test_data["2"])

    def tearDown(self):
        self.driver.quit()
        
def read_test_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
    
if __name__ == '__main__':
    test_data = read_test_data('test_data.json')

    template_args = {
        "user": getpass.getuser(),
        "data": test_data,
    }

    h = HtmlTestRunner.HTMLTestRunner(template='../../Template/templateReport.html', template_args=template_args)
    unittest.main(testRunner=h)
