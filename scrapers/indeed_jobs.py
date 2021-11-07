import time
import urllib.parse
from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_indeed_jobs_by_search_terms(jobs_search_terms, on_site_or_remote_jobs):
	# Here we will save the jobs count for every search term
	jobs_found_results = [];

	# URL for the indeed jobs
	url = "https://www.indeed.com/jobs?";

	# Create different GET requests for 'on_site' and 'remote' job types
	if on_site_or_remote_jobs == 'on_site':
		url += 'q='
	elif on_site_or_remote_jobs == 'remote':
		# Filter only by the remote jobs
		url += 'remotejob=032b3046-06a3-4876-8dfd-474eb5e7ed11&q='
	else :
		print('Bad input, please select either "on_site" or "remote" without the quotes! Exiting from the program!')
		exit()

	# Search by every search term
	for search_term in jobs_search_terms:
		# Add the search term to the url
		url_specific = url + urllib.parse.quote(search_term);

		# Create get request with the search term
		page = urlopen(url_specific)
		html = page.read().decode("utf-8")

		# Create BeatifulSoup object to get html data easier from the html response
		soup = BeautifulSoup(html, "html.parser")

		# Search for <div id="searchCountPages"></div> and get the text in it
		jobs_count_element = soup.find("div", {"id" : "searchCountPages"})
		
		# HTML element found
		if jobs_count_element is not None:
			jobs_count_text = jobs_count_element.text

			# We have this text now "Page 1 of 2,358 jobs" and we are converting it to "2,358"
			jobs_count_text = ((jobs_count_text.split("of "))[1]).split(" jobs")[0]

			# We have this text now "2,358" so we convert it to "2358" and integer
			jobs_count = int(jobs_count_text.replace(",", ""))
		# HTML element not found
		else:
			jobs_count = 0

		jobs_found_results.append(jobs_count);

		# Create the next request after 2 seconds in order to not be detected as a bot
		time.sleep(2)

	return jobs_found_results
