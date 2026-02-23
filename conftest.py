from selenium import webdriver
import pytest

try:
    from webdriver_manager.chrome import ChromeDriverManager
except Exception:
    ChromeDriverManager = None


@pytest.fixture(scope="function")
def selenium(request):
    """Provide a selenium webdriver.Chrome instance using webdriver-manager.

    This overrides pytest-selenium's default `selenium` fixture so tests don't
    require a preinstalled chromedriver binary in PATH.
    """
    options = webdriver.ChromeOptions()
    # run headless by default for CI and local tests
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    if ChromeDriverManager is None:
        # Fallback: rely on system chromedriver in PATH
        driver = webdriver.Chrome(options=options)
    else:
        driver_path = ChromeDriverManager().install()
        driver = webdriver.Chrome(executable_path=driver_path, options=options)

    yield driver
    try:
        driver.quit()
    except Exception:
        pass
