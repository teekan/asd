import time
import subprocess
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.headless = True
def hit():
	try:
		browser = webdriver.Firefox(options=opts)
		browser.get("http://www.slutbags.tk")
		body = browser.find_elements_by_class_name("text-center")
		print(browser.title)
		print(body[0])
		body[0].click()
		browser.switch_to.window(browser.window_handles[1])
		print(browser.title)
		ad = browser.find_elements_by_tag_name("iframe")
		print(ad[0])
		ad[0].click()
		time.sleep(2)
		browser.switch_to.window(browser.window_handles[1])
		print(browser.title)
		print(ad[1])
		ad[1].click()
		time.sleep(2)
		browser.switch_to.window(browser.window_handles[1])
		print(browser.title)
		for x in browser.window_handles:
			browser.switch_to.window(x)
			browser.close()
		print("Finished clicking")
		subprocess.run(['./track.sh'])
	except:
		print("except is running")
		subprocess.run(['./crash.sh'])
		subprocess.run(['./clean.sh'])

while True:
	hit()
