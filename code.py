import subprocess
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.headless = True
while True:
	try:
		browser = webdriver.Firefox(options=opts)
		browser.get("http://www.slutbags.tk")
		ads = browser.find_elements_by_tag_name("iframe")
		print(ads[0])
		ads[0].click()
		browser.switch_to.window(browser.window_handles[0])
		print(ads[1])
		ads[1].click()
		browser.switch_to.window(browser.window_handles[0])
		body = browser.find_elements_by_tag_name("body")
		print(body[0])
		body[0].click()
		browser.switch_to.window(browser.window_handles[1])
		for x in browser.window_handles:
			browser.switch_to.window(x)
			browser.close()
		subprocess.run(['./track.sh'])
	except:
		subprocess.run(['./crash.sh'])
		subprocess.run(['./clean.sh'])
		subprocess.run(['python3','code.py'])
