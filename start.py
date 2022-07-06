from random import randint
import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

profile_path = r"dir"
profile = r"profile"
user_agent = "user agent"

options = uc.ChromeOptions()

with open("proxy.txt") as f:
    lines = f.readlines()

proxy_raw = lines[randint(0, len(lines)) - 1].split(":")
PROXY = f"http://{proxy_raw[0]}:{proxy_raw[1]}"
options.add_argument('--proxy-server=%s' % PROXY)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument(f"user-data-dir={profile_path}")
options.add_argument(f'profile-directory={profile}')
options.add_argument(f'user-agent={user_agent}')
driver = uc.Chrome(options=options)

with driver:
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.get("url")
    driver.implicitly_wait(5)

    try:
        element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, 'xpath')))
    except(TimeoutException, NoSuchElementException, ElementNotVisibleException):
        pass
