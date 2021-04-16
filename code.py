import subprocess
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.headless = True
def hit():
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
		body = browser.find_elements_by_class_name("text-center")
		print(body[0])
		body[0].click()
		browser.switch_to.window(browser.window_handles[1])
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
