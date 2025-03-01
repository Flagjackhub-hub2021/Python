from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
 
 
def getUrl2Screenshot(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
 
    driver = webdriver.Chrome()
 
    driver.get(url)
    time.sleep(2)
    width = 1920
    height = 1080
    driver.set_window_size(width,height)
    driver.execute_script('window.scrollBy(0,500)')
    time.sleep(2)
    driver.save_screenshot("ourscreenshot.png")
    driver.quit()
 
 
targetUrl = "https://www.instagram.com/merdekasiber/"
getUrl2Screenshot(targetUrl)