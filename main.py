from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# import Selenium
# download ChromeDriver - https://chromedriver.chromium.org/downloads

# useful links for selenium errors
# https://stackoverflow.com/questions/69875125/find-element-by-commands-are-deprecated-in-selenium
# https://stackoverflow.com/questions/10251525/how-can-i-get-the-current-contents-of-an-element-in-webdriver/43047867#43047867

service = Service(r"C:\\Users\\janns\\PycharmProjects\\chromedriver.exe")
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

# ----------------------------------------------------------------------------------------------------------------------

# EXAMPLE USE OF SELENIUM TO FIND ELEMENTS ON A WEBPAGE

# getting the price of instant pot from amazon -------------------------------------------------------------------------
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
# price_symbol = driver.find_element(By.CLASS_NAME, "a-price-symbol")
# price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(f"{price_symbol.text}{price_whole.text}")

# getting the tag name and attribute of search bar in python.org -------------------------------------------------------
# driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# getting the size of python logo from python.org ----------------------------------------------------------------------
# driver.get("https://www.python.org/")
# python_logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(python_logo.size)

# getting the documentation link from python.org -----------------------------------------------------------------------
# driver.get("https://www.python.org/")
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# # getting the 'submit website bug' link using xpath from python.org --------------------------------------------------
# driver.get("https://www.python.org/")
# website_bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(website_bug_link.text)

# ----------------------------------------------------------------------------------------------------------------------

# GETTING THE EVENT WIDGET FROM PYTHON.ORG

driver.get("https://www.python.org")
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

for event in range(len(events)):
    print(events[event])

driver.quit()
