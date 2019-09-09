from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import urllib3


opts = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
opts.add_argument(f'user-agent={userAgent}')
opts.add_argument("--enable-javascript")


browser = webdriver.Chrome(chrome_options=opts)
#executable_path='/Users/calvintruong/weber/bin'
#executable_path=r'C:\WebDrivers\ChromeDriver\chromedriver_win32\chromedriver.exe'

#browser.get('https://www.yellowpages.com/')
browser.get('https://www.yellowpages.com/search?search_terms=pool&geo_location_terms=Los+Angeles%2C+CA')

#elem = browser.find_element_by_id('query')  # Find the search box
#elem.send_keys('pool')
#elem = browser.find_element_by_id('location')
#elem.clear()
#elem.send_keys('dallas' + Keys.RETURN)

quotePage = browser.current_url
http = urllib3.PoolManager()
page = http.request('GET', quotePage)


soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find('h2', attrs={'class’: ‘name'} )
name = name_box.text.strip() # strip() is used to remove starting and trailing
print (name)



input("Press Enter to continue...")
browser.close()