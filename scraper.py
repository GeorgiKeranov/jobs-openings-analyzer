import os
import pickle
import time
import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Scraper:
	# Here we will save all references of the html elements that we have found
	selenium_elements = {}

	# This delay is used when we are waiting for element to get loaded in the html
	find_element_delay = 20

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

		self.go_to_page(self.url)


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
		# Go to login page
		self.go_to_page(self.login_url)

		# Ask for username in the terminal for secure reasons
		username = getpass.getpass('Username: ')
		# Ask for password in the terminal for secure reasons
		password = getpass.getpass()

		self.element_send_keys(self.username_selector, username)
		self.element_send_keys(self.password_selector, password)
		
		if self.remember_checkbox_selector:
			self.element_click(self.remember_checkbox_selector)
		
		time.sleep(10)
		self.save_cookies()

	# Wait random amount of seconds before taking some action so the server won't be able to tell if you are a bot
	def wait_random_time():
		random_sleep_seconds = round(random.uniform(1.00, 4.00), 2)

		time.sleep(random_sleep_seconds)

	# Goes to a given page and waits random time before that to prevent detection as a bot
	def go_to_page(self, page):
		# Wait random time before refreshing the page to prevent the detection as a bot
		self.wait_random_time()

		# Refresh the site url with the loaded cookies so the user will be logged in
		self.driver.get(page)

	def find_element(self, selector):
		# Check if we already have found this element and return the element
		if selector in self.selenium_elements.keys():
			return self.selenium_elements[selector]

		try:
			# Wait for element to load for some time declared in 'find_element_delay'
			element = WebDriverWait(driver, self.find_element_delay).until(EC.presence_of_element_located(By.CSS_SELECTOR, selector))
		except TimeoutException:
			print('ERROR: Timed out waiting for the element with css selector "{selector}" to load')

			# End the program execution because we cannot find the element
			exit()
		
		# Add this element in the global dictionary so if we need it multiple times
		# we will not have to search for it in the html
		self.selenium_elements[selector] = element

		return element

	# Find element based on 'selector' variable and wait some random time before clicking it
	def element_click(self, selector):
		element = self.find_element(selector)

		self.wait_random_time()

		element.click()

	# Find element based on 'selector' variable and wait some random time before typing the text in it
	def element_send_keys(self, selector, text):
		element = self.find_element(selector)

		self.wait_random_time()

		element.send_keys(text)

	# Find element based on 'selector' variable and wait some random time before clearing the value from element
	def element_clear(self, selector):
		element = self.find_element(selector)

		self.wait_random_time()

		element.clear()
