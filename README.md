# DuckDuckGo-Search-Automation-with-Selenium-Pytest

This project demonstrates end-to-end UI test automation for the DuckDuckGo search engine using Selenium WebDriver, Pytest, and a Page Object Model (POM) design pattern. It is designed for clarity, extensibility, and configurability.

* Features

- Clean Page Object Model for test maintainability
-  Pytest test runner with parametrized test cases
-  Browser config via config.json (supports Firefox, Chrome, Headless Chrome)
-   Implicit waits and explicit waits to handle dynamic content
-   Easily extendable with new search terms or test cases


* Technologies

Python 3.13+
Selenium WebDriver
Pytest
Firefox or Chrome (via WebDriver)


* Example Test Case
  
pytest -v tests/test_search.py

This will search for phrases like panda, python, and polar bear, and verify:

The input box retains the search query
The result titles are relevant
The page title contains the search phrase


* Supported browsers:

"Firefox"
"Chrome"
"Headless Chrome"
