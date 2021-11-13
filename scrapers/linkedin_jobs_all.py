import time
import urllib.parse
from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_all_linkedin_jobs_by_search_terms(jobs_search_terms):
	# Here we will save the jobs count for every search term
	jobs_found_results = []

	# URL for the LinkedIn jobs that are worldwide
	url = "https://www.linkedin.com/jobs/search?location=Worldwide&locationId=&geoId=92000000&f_TPR=&position=1&pageNum=0&keywords="

	# Search by every search term
	for search_term in jobs_search_terms:
		# Add the search term to the url
		url_specific = url + urllib.parse.quote(search_term)
		
		# Create get request with the search term
		try:
			# Page is found
			page = urlopen(url_specific)
		except:
			# Page is not found
			print('Page not found, please check the URL - ' + url_specific)
			jobs_found_results.append(0)
			continue

		# Create BeatifulSoup object to get html data easier from the html response
		html = page.read().decode("utf-8")
		soup = BeautifulSoup(html, "html.parser")

		# Search for <label for="f_TRP-3"></label>
		jobs_count_element = soup.find("label", {"for" : "f_TPR-3"})

		# HTML element is not found
		if jobs_count_element is None:
			jobs_found_results.append(0)
			time.sleep(3)
			continue

		# Get the text from the HTML element
		jobs_count_text = jobs_count_element.text

		# We have this text now "Any Time (143,727)" and we are converting it to "143,727"
		jobs_count_text = ((jobs_count_text.split("("))[1]).split(")")[0]

		# We have this text now "143,727" so we convert it to "143727" and integer
		jobs_count = int(jobs_count_text.replace(",", ""))

		jobs_found_results.append(jobs_count)

		# Create the next request after 3 seconds in order to not be detected as a bot
		time.sleep(3)

	return jobs_found_results
