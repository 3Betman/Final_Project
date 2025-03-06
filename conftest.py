import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Добавление параметра language
# Добавляется опция --language в pytest.
# Значение переданного языка ("ru", "en", "fr", "es") будет доступно через request.config.getoption("language").


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: '--language=en' or '--language=ru' or '--language=fr' or '--language=es'")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language") #Получаем переданный язык через request.config.getoption("language").
    options = Options()                                  #Создаём объект Options() для конфигурации браузера Chrome.

    # Добавляем экспериментальную настройку prefs
    # Это указывает Chrome, какой язык использовать в интерфейсе и заголовках HTTP Accept-Language.
    # Например, если user_language="ru", Chrome будет запрашивать страницы на русском языке.

    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
