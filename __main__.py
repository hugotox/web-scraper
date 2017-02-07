import os
import settings
from selenium.webdriver import PhantomJS
from causas_page.page import CausasPage
from main_page.page import MainPage

driver = PhantomJS(os.path.join(os.getcwd(), 'drivers', 'phantomjs'))
driver.set_window_size(1200, 775)

main_page = MainPage(driver, rut=settings.RUT, clave=settings.CLAVE)
main_page.open()
main_page.login()

causas = CausasPage(driver)
causas.open()
causas.init_scraping()  # start the background process

driver.quit()
