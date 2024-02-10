"""
    Selenium
"""
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
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
    # Exemple
    options = ()  # ('--disable-gpu', '--no-sandbox')
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com.br')
    sleep(30)
