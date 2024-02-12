"""
    Selenium
"""
# type: ignore
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    """
        Configurar o drive do navegador
    """
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROMEDRIVER_EXEC)
    )
    chrome_browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return chrome_browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10
    # Exemple
    options = ()  # ('--disable-gpu', '--no-sandbox')
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com.br')

    # Espera para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.NAME, 'q')))

    search_input.send_keys('Hello World!')
    search_input.send_keys(Keys.ENTER)

    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)
