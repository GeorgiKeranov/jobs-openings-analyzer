import time
from scraper import Scraper
from selenium.webdriver.common.keys import Keys
from visualize_data import visualize_data

def scrape_number_of_jobs_by_each_search_term(search_terms):
	results_for_search_terms = []

	# Go to linkedin and login with username and password or cookies if we have already logged in
	scraper = Scraper('https://www.linkedin.com')
	scraper.add_login_functionality('https://www.linkedin.com/login', '#username', '#password', '', 'button[type="submit"]', 'linkedin')

	time.sleep(2)
	search_input = scraper.find_element('.search-global-typeahead__input')
	search_input.click()

	time.sleep(2)
	search_input.send_keys(search_terms[0] + Keys.ENTER)

	time.sleep(5)
	jobs_button = scraper.find_element('button[aria-label="Jobs"]')
	jobs_button.click()

	time.sleep(1)
	location_input = scraper.find_element('input[aria-label="City, state, or zip code"]')
	location_input.click()

	time.sleep(2)
	location_input.clear()
	location_input.send_keys('Worldwide' + Keys.ENTER)

	time.sleep(2)
	onsite_remote_button = scraper.find_element('button[aria-label="On-site/Remote filter. Clicking this button displays all On-site/Remote filter options."]')
	onsite_remote_button.click()

	time.sleep(1)
	remote_jobs_label = scraper.find_element('label[for="workplaceType-2"]')
	remote_jobs_label.click()

	time.sleep(2)
	show_results_button = scraper.find_element('.artdeco-hoverable-content--visible button[data-control-name="filter_show_results"]')
	show_results_button.click()

	time.sleep(3)
	results = scraper.find_element('.jobs-search-results-list__title-heading small');
	results_number_text = (results.text).split(' ')[0]
	results_number = int(results_number_text.replace(',', ''))
	results_for_search_terms.append(results_number)

	for index, search_term in enumerate(search_terms):
		if index == 0:
			continue;

		time.sleep(2)
		search_input = scraper.find_elements('.jobs-search-box__keyboard-text-input')[0]
		search_input.click()
		time.sleep(2)
		search_input.clear()
		search_input.send_keys(search_term + Keys.ENTER)

		time.sleep(3)
		results = scraper.find_element('.jobs-search-results-list__title-heading small');
		results_number_text = (results.text).split(' ')[0]
		results_number = int(results_number_text.replace(',', ''))
		results_for_search_terms.append(results_number)
  
	return results_for_search_terms;

search_terms = [
	'Spring Boot',
	'Laravel',
	'Ruby on Rails',
	'Django',
	'Express.js',
	'Node.js'
]

results_for_search_terms = scrape_number_of_jobs_by_each_search_term(search_terms)

print(search_terms)
print(results_for_search_terms)

visualize_data_in_pie_chart(results_for_search_terms, search_terms)
