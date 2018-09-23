import selenium
from selenium import webdriver
import time

chromedriver_path = "/Users/Avesa/PycharmProjects/01000010ot_col/chromedriver"

driver = webdriver.Chrome(chromedriver_path)
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)

driver.get("https://www.instagram.com/trippy")
pics = driver.find_elements_by_xpath('''//body/span/section/main/div/div[3]/article/div/div/div''')
print(len(pics))
time.sleep(60)

get_dad = "420!!!!!"