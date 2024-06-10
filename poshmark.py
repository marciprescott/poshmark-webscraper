from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.manager.chrome import ChromeDriverManager

#  class="search-box-con"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


web = "https://poshmark.com/category/Women"
path = "/Users/marciprescott/Downloads/chromedriver-mac-arm64 4/chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
# Open chromedriver and open website
driver.get(web)
driver.implicitly_wait(0.5)
text_box = driver.find_element(By.ID, "searchInput")
text_box.send_keys("Prada Black Brushed Leather loafers size 9")
text_box.send_keys(Keys.RETURN)
driver.implicitly_wait(0.5)
driver.quit()
