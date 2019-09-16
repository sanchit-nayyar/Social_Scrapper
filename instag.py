from selenium import webdriver
from bs4 import BeautifulSoup
import urllib, time

profile = webdriver.FirefoxProfile('/home/sanchit/.mozilla/firefox/scus57fc.default')
ffx = webdriver.Firefox(profile)
profile_url = 'https://www.instagram.com/shreyaa_singh9/'
ffx.get(profile_url)

SCROLL_PAUSE_TIME = 5.0
last_height = ffx.execute_script("return document.body.scrollHeight")
while True:
	ffx.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(SCROLL_PAUSE_TIME)
	new_height = ffx.execute_script("return document.body.scrollHeight")
	if new_height == last_height:
		break
	last_height = new_height

soup = BeautifulSoup(ffx.page_source, 'html.parser')

pic_id = 0

for img in soup.find_all('img'):
	print img['src']
	pic_id += 1

	urllib.urlretrieve(img['src'], 'img' + str(pic_id) + '.jpg')

# print ffx.find_element_by_tag_name('img')
ffx.close()
