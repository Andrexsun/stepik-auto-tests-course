import time
from selenium import webdriver
import math
from selenium.webdriver.common.by import By

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/math.html")
	x_element = browser.find_element_by_css_selector('#input_value')
	x = x_element.text
	
	print(x)
	def calc(x):
  		return str(math.log(abs(12*math.sin(int(x)))))
	
	y = calc(x)

	input1 = browser.find_element_by_css_selector('#answer')
	input1.send_keys(y)
	click1 = browser.find_element_by_css_selector('#robotCheckbox')
	click1.click()
	click2 = browser.find_element_by_css_selector('#robotsRule')
	click2.click()
	click3 = browser.find_element_by_css_selector('button.btn.btn-default')
	click3.click()

finally:
	pass
	#browser.quit()

