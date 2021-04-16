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
		ads[0].click()
		browser.switch_to.window(browser.window_handles[0])
		ads[1].click()
		browser.switch_to.window(browser.window_handles[0])
		body = browser.find_elements_by_tag_name("body")
		body[0].click()
		for x in browser.window_handles:
			browser.switch_to.window(x)
			browser.close()
	except:
		subprocess.run(['sudo','./crash.sh'])
		subprocess.run(['sudo','./clean.sh'])
		subprocess.run(['sudo','python3','code.py'])
	subprocess.run(['./track.sh'])
