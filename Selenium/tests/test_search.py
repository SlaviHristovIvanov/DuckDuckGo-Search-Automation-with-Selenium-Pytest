import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for the given phrase
    search_page.search(phrase)

    # Wait until the title contains the phrase
    WebDriverWait(browser, 10).until(EC.title_contains(phrase))

    # ✅ Wait until at least one result link is present
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a.result__a'))
    )

    # Then the search result query is the phrase
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to the phrase
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # And the search result title contains the phrase
    assert phrase in result_page.title()

