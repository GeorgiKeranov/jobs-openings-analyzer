import os
import pickle
import time
import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Scraper:
	def __init__(self, url):
		self.url = url

		self.setup_driver_options()
		self.setup_driver()

	def __del__(self):
		if hasattr(self, 'cookies_file_path'):	
			self.save_cookies()

		self.driver.close()

	def setup_driver_options(self):
		self.driver_options = Options()

		arguments = [
			'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
			'--start-maximized',
			'--disable-blink-features=AutomationControlled'
		]

		experimental_options = [
			{'key': 'excludeSwitches', 'value': ['enable-automation', 'enable-logging']},
		]

		for argument in arguments:
			self.driver_options.add_argument(argument)

		for experimental_option in experimental_options:
			self.driver_options.add_experimental_option(experimental_option['key'], experimental_option['value'])

	def setup_driver(self):
		self.driver = webdriver.Chrome(options = self.driver_options)
		self.driver.get(self.url)

	def add_login_functionality(self, login_url, username_selector, password_selector, remember_checkbox_selector, login_button_selector, cookies_file_name):
		self.login_url = login_url
		self.username_selector = username_selector
		self.password_selector = password_selector
		self.remember_checkbox_selector = remember_checkbox_selector
		self.login_button_selector = login_button_selector
		self.cookies_file_path = 'cookies_files/' + cookies_file_name + '.pkl'

		self.load_cookies()

	def load_cookies(self):
		if not os.path.isfile(self.cookies_file_path):
			self.login()
			return
		
		cookiesFile = open(self.cookies_file_path, 'rb')
		cookies = pickle.load(cookiesFile)
		
		for cookie in cookies:
			self.driver.add_cookie(cookie)

		cookiesFile.close()

		self.wait_random_time()
		self.driver.get(self.url)

	def save_cookies(self):
		cookiesFile = open(self.cookies_file_path, 'wb')
		cookies = self.driver.get_cookies()

		pickle.dump(cookies, cookiesFile)

		cookiesFile.close()

	def login(self):
		self.wait_random_time()

		self.driver.get(self.login_url)

		try:
			username_field = self.driver.find_element_by_css_selector(self.username_selector)
			password_field = self.driver.find_element_by_css_selector(self.password_selector)
			login_button = self.driver.find_element_by_css_selector(self.login_button_selector)

			if self.remember_checkbox_selector:
				remember_checkbox = self.driver.find_element_by_css_selector(self.remember_checkbox_selector)
		except:
			print('Some of the html elements is not found, please check the selectors in add_login_functionality()')
			return

		username = getpass.getpass('Username: ')
		username_field.send_keys(username)
		
		password = getpass.getpass()
		password_field.send_keys(password)
		
		if 'remember_checkbox' in locals():
			self.wait_random_time()
			remember_checkbox.click()

		self.wait_random_time()
		login_button.click()

		self.wait_random_time()
		self.save_cookies()

	def find_element(self, selector):
		return self.driver.find_element_by_css_selector(selector)

	def find_elements(self, selector):
		return self.driver.find_elements_by_css_selector(selector)

	def wait_random_time():
		random_sleep_seconds = round(random.uniform(1.0, 4.0), 2)

		time.sleep(random_sleep_seconds)
