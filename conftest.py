import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Write the language you want to use")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': "user_language"})
    browser = webdriver.Chrome(options=options)
    print("\nstart browser for test..")
    yield browser
    print("\nquit browser.." + user_language)
    browser.quit()
    
    
