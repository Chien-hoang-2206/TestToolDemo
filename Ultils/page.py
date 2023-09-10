from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import pdb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_for_error_script(driver):
    try:
        # Wait for the element to be present before trying to find it
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="webpack-dev-server-client-overlay-div"]/div[1]'))
        )
    except NoSuchElementException:
        pdb.set_trace()
        print("Phát hiện phần tử error_Scripy trong test case. In thông báo.")
