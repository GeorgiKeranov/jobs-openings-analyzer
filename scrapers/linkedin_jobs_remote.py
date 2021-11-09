import time
from helpers.scraper import Scraper
from selenium.webdriver.common.keys import Keys

def get_remote_linkedin_jobs_by_search_terms(jobs_search_terms):
	jobs_found_results = []

	# Initialize the scraper for linkedin
	scraper = Scraper('https://www.linkedin.com')

	# Add login functionality to the scraper
	scraper.add_login_functionality('https://www.linkedin.com/login', '.global-nav__me-photo.ember-view', 'linkedin')

	# Enter the first search term in the search bar
	search_input_selector = '.search-global-typeahead__input'
	scraper.element_send_keys(search_input_selector, jobs_search_terms[0] + Keys.ENTER)

	# Filter search results by jobs
	jobs_button_selector = 'button[aria-label="Jobs"]'
	scraper.element_click(jobs_button_selector)

	# Filter search results location to be WorldWide
	location_input_selector = 'input[aria-label="City, state, or zip code"]'
	scraper.element_clear(location_input_selector)
	scraper.element_send_keys(location_input_selector, 'Worldwide' + Keys.ENTER)

	# Filter the jobs to only Remote ones
	onsite_remote_button_selector = 'button[aria-label="On-site/Remote filter. Clicking this button displays all On-site/Remote filter options."]'
	remote_jobs_label_selector = 'label[for="workplaceType-2"]'
	show_results_button_selector = '.artdeco-hoverable-content--visible button[data-control-name="filter_show_results"]'
	scraper.element_click(onsite_remote_button_selector)
	scraper.element_click(remote_jobs_label_selector)
	scraper.element_click(show_results_button_selector)

	# Wait until the new jobs count is loaded
	time.sleep(5)

	# Get HTML elment for number of jobs found
	jobs_found_element = scraper.find_element('.jobs-search-results-list__title-heading small', False, 10)

	# HTML element is found
	if jobs_found_element:
		jobs_found_text = (jobs_found_element.text).split(' ')[0]
		jobs_found_number = int(jobs_found_text.replace(',', ''))
	# HTML element is not found
	else:
		jobs_found_number = 0

	jobs_found_results.append(jobs_found_number)

	search_input_jobs_selector = '.jobs-search-box__input--keyword .relative input:nth-child(2)'

	for index, search_term in enumerate(jobs_search_terms):
		if index == 0:
			continue;

		scraper.element_clear(search_input_jobs_selector)
		scraper.element_send_keys(search_input_jobs_selector, search_term + Keys.ENTER)

		# Wait until the new jobs count is loaded
		time.sleep(5)

		# Get HTML elment for number of jobs found
		jobs_found_element = scraper.find_element('.jobs-search-results-list__title-heading small', False, 10)

		# HTML element is found
		if jobs_found_element:
			jobs_found_text = (jobs_found_element.text).split(' ')[0]
			jobs_found_number = int(jobs_found_text.replace(',', ''))
		# HTML element is not found
		else:
			jobs_found_number = 0

		jobs_found_results.append(jobs_found_number)

	scraper.save_cookies()

	return jobs_found_results
