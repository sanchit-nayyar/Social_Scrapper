from selenium import webdriver
import urllib, time

def scrolling(browser):
	SCROLL_PAUSE_TIME = 3.0
	last_height = browser.execute_script("return document.body.scrollHeight")
	for i in range(7):
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(SCROLL_PAUSE_TIME)
		new_height = browser.execute_script("return document.body.scrollHeight")
		if new_height == last_height:
			break
		last_height = new_height


profile = webdriver.FirefoxProfile('/home/sanchit/.mozilla/firefox/scus57fc.default')
ffx = webdriver.Firefox(profile)
image_url = 'https://www.facebook.com/mitali.srivastava.391/photos?lst=100002220838238%3A100001842942262%3A1530027370&source_ref=pb_friends_tl'
ffx.get(image_url)
scrolling(ffx)
pics = ffx.find_elements_by_class_name('uiMediaThumbImg')
n_pics = len(ffx.find_elements_by_class_name('uiMediaThumbImg'))
for pic_id in range(n_pics):
	try:
		pics[pic_id].click()
		urllib.urlretrieve(ffx.find_elements_by_class_name('spotlight')[0].get_attribute('src'), 'img' + str(pic_id) + '.jpg')
		ffx.get(image_url)
		scrolling(ffx)
		pics = ffx.find_elements_by_class_name('uiMediaThumbImg')
	except:
		pass

ffx.close()