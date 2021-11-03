import os
import pickle
import time
import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Scraper:
	selenium_elements = {}

	def __init__(self, url):
		self.url = url

		self.setup_driver_options()
		self.setup_driver()

	# Automatically save cookies and close driver on destruction of the object
	def __del__(self):
		if hasattr(self, 'cookies_file_path'):	
			self.save_cookies()

		self.driver.close()

	# Add these options in order to make chrome driver appear as a human instead of detecting it as a bot
	# Also change the 'cdc_' string in the chromedriver.exe with Notepad++ for example with 'abc_' to prevent detecting it as a bot
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

	# Setup chrome driver with predefined options
	def setup_driver(self):
		self.driver = webdriver.Chrome(options = self.driver_options)
		self.driver.get(self.url)

	# Add login functionality and load cookies if there are any with 'cookies_file_name'
	def add_login_functionality(self, login_url, username_selector, password_selector, remember_checkbox_selector, login_button_selector, cookies_file_name):
		self.login_url = login_url
		self.username_selector = username_selector
		self.password_selector = password_selector
		self.remember_checkbox_selector = remember_checkbox_selector
		self.login_button_selector = login_button_selector
		self.cookies_file_path = 'cookies_files/' + cookies_file_name + '.pkl'

		self.load_cookies()

	# Load cookies from file
	def load_cookies(self):
		# If there is no file with cookies go to the login page and ask for credentials
		if not os.path.isfile(self.cookies_file_path):
			self.login()
			return
		
		# Load cookies from the given file name in 'add_login_functionality' function
		cookies_file = open(self.cookies_file_path, 'rb')
		cookies = pickle.load(cookies_file)
		
		for cookie in cookies:
			self.driver.add_cookie(cookie)

		cookies_file.close()

		# Wait random time before refreshing the page to prevent the detection as a bot
		self.wait_random_time()
		# Refresh the site url with the loaded cookies so the user will be logged in
		self.driver.get(self.url)


	# Save cookies to file
	def save_cookies(self):
		# Open or create cookies file with the given name from 'add_login_functionality'
		cookies_file = open(self.cookies_file_path, 'wb')
		
		# Get current cookies from the driver
		cookies = self.driver.get_cookies()

		# Save cookies in the cookie file as a byte stream
		pickle.dump(cookies, cookies_file)

		cookies_file.close()

	# Go to login page and asks for credentials to log in the user then saves the cookies
	def login(self):
		self.wait_random_time()

		# Go to login page
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

		# Ask for username in the terminal for secure reasons
		username = getpass.getpass('Username: ')
		username_field.send_keys(username)
		
		# Ask for password in the terminal for secure reasons
		password = getpass.getpass()
		password_field.send_keys(password)
		
		if self.remember_checkbox_selecto:
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
