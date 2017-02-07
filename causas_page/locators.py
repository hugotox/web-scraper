from selenium.webdriver.common.by import By


class CausasPageLocators(object):

    # every tab has 10 rows of forms, all of them with the same action
    FORMS_XPATHS = [
        (By.XPATH, "//form[@action='./causas/causa_suprema2.php']"),
        (By.XPATH, "//form[@action='./causas/causa_corte2.php']"),
        (By.XPATH, "//form[@action='./causas/causaCivil2.php']"),
        (By.XPATH, "//form[@action='./causas/causa_laboral_reformado2.php']"),
        (By.XPATH, "//form[@action='./causas/causa_penal2.php']"),
        (By.XPATH, "//form[@action='./causas/causa_cobranza2.php']"),
        (By.XPATH, "//form[@action='./causas/causaFamilia2.php']"),
    ]

    PAGINATION_NEXT = [
        (By.ID, 'suprema_siguiente'),
        (By.ID, 'corte_siguiente'),
        (By.ID, 'civil_siguiente'),
        (By.ID, 'laboral_siguiente'),
        (By.ID, 'penal_siguiente'),
        (By.ID, 'cobranza_siguiente'),
        (By.ID, 'familia_siguiente'),
    ]

