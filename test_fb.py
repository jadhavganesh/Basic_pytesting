from selenium import webdriver
import time
def test_fb():
	browser=webdriver.Firefox()
	browser.get('https://facebook.com')
	email = browser.find_element_by_id("email")
	email.send_keys("Enter the your email id or Mobile number")
	passd = browser.find_element_by_id("pass")
	passd.send_keys("Enter the password of facebook")
	click = browser.find_element_by_id("loginbutton")
	click.click()

test_fb()
