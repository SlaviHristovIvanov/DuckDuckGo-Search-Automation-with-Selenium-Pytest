from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage:

    # URL
    URL = "https://duckduckgo.com"

    SEARCH_INPUT = (By.NAME, "q")

    def __init__(self, browser):  # fixed typo here
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
