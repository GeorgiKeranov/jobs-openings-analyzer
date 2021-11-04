from scrapers.indeed_jobs import get_indeed_jobs_by_search_terms
from scrapers.linkedin_jobs_on_site import get_on_site_linkedin_jobs_by_search_terms
from scrapers.linkedin_jobs_remote import get_remote_linkedin_jobs_by_search_terms
from helpers.visualize_data import visualize_data_in_pie_chart

# Get all jobs search terms in 'jobs_search_terms.txt' file and convert them into array
jobs_search_terms = []
with open('jobs_search_terms.txt') as jobs_search_terms_file:
	jobs_search_terms = [line.strip() for line in jobs_search_terms_file.readlines()]


# indeed_on_site_jobs_count = get_indeed_jobs_by_search_terms(jobs_search_terms)
# indeed_remote_jobs_count = get_indeed_jobs_by_search_terms(jobs_search_terms, 'remote')

# linkedin_on_site_jobs_count = get_on_site_linkedin_jobs_by_search_terms(jobs_search_terms)
# linkedin_jobs_remote = get_remote_linkedin_jobs_by_search_terms(jobs_search_terms)

# visualize_data_in_pie_chart()
