import settings
from causas_page.popup import Popup
from core.base_page import BasePage
from causas_page.locators import CausasPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CausasPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, 'https://oficinajudicialvirtual.pjud.cl/busqueda_por_rut.php')
        self.main_window = None

    def loop_forms(self, forms, locator):
        driver = self.driver
        for form in forms:
            print('Submitting form {}...'.format(locator[1]))
            form.submit()
            # wait to make sure there are two windows open
            WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 2)

            # switch windows
            driver.switch_to.window('popup')

            popup = Popup(self.driver)
            popup.check_data()
            driver.switch_to.window(self.main_window)

            # TODO: go to next page until there is no "Siguiente" link

    def init_scraping(self):
        driver = self.driver
        self.main_window = driver.current_window_handle

        # tab content is loaded using ajax so we need to wait for it...
        for locator in CausasPageLocators.FORMS_XPATHS:
            WebDriverWait(driver, settings.WEB_DRIVER_WAIT_TIMEOUT).until(
                EC.presence_of_element_located(locator)
            )

            forms = driver.find_elements(*locator)
            self.loop_forms(forms, locator)
