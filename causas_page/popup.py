from core.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class PopupLocators(object):
    TABS = (By.ID, 'tabs')
    TABLE = (By.CSS_SELECTOR, '.tablaPop')


class Popup(BasePage):
    def __init__(self, driver):
        super().__init__(driver, '')

    def check_data(self):
        driver = self.driver

        # wait to make sure the new window is loaded
        WebDriverWait(driver, 10).until(lambda d: d.find_element(*PopupLocators.TABS) is not None)

        # there are 2 tables with the same class, first one is the documents table
        table = driver.find_elements(*PopupLocators.TABLE)[0]

        # first row is heading
        heading = True
        rows = table.find_elements_by_tag_name('tr')
        for row in rows:
            if not heading:
                cols = row.find_elements_by_tag_name('td')
                data = ' - '.join([col.text for col in cols])
                print(data)
            heading = False

        # driver.close()  # needed when using Chrome
