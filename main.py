from scrapers.indeed_jobs import get_indeed_jobs_by_search_terms
from scrapers.linkedin_jobs_on_site import get_on_site_linkedin_jobs_by_search_terms
from scrapers.linkedin_jobs_remote import get_remote_linkedin_jobs_by_search_terms
from helpers.visualize_data import visualize_data_in_grouped_bar_chart
from helpers.visualize_data import visualize_data_in_bar_chart

# Get all jobs search terms in 'jobs_search_terms.txt' file and convert them into array
jobs_search_terms = []
with open('jobs_search_terms.txt') as jobs_search_terms_file:
	jobs_search_terms = [line.strip() for line in jobs_search_terms_file.readlines()]

if not jobs_search_terms:
	print('Please add all of the search terms that you want to search by in "jobs_search_terms.txt" file in the main directory.\n')
	print('Please note that each term have to be on new line.')
	exit()

site_to_get_data_from = input('Which site you want to get data from, these are the options:\n - linkedin\n - indeed\n\nFetch data from: ')
allowed_sites = ['linkedin', 'indeed']

if not site_to_get_data_from in allowed_sites:
	print('\nIncorrect option selected, please check the options again')
	exit()

type_of_jobs = input('\nWhich types of jobs you want, these are the options:\n - on-site\n - remote\n - both\n\nTypes of jobs: ')
allowed_types_of_jobs = ['on-site', 'remote', 'both']

if not type_of_jobs in allowed_types_of_jobs:
	print('\nIncorrect option selected, please check the options again')
	exit()
else:
	print('\nPlease wait, it may take a while to scrape all the data from the site')

chart_title = 'Job Openings in ' + site_to_get_data_from.capitalize()
if type_of_jobs is not 'both':
	chart_title = type_of_jobs.capitalize() + ' ' + chart_title

# TODO fix these ugly if conditions with something more dynamic
if type_of_jobs == 'on-site':
	if site_to_get_data_from == 'linkedin':
		jobs_count = get_on_site_linkedin_jobs_by_search_terms(jobs_search_terms)
	if site_to_get_data_from == 'indeed':
		jobs_count = get_indeed_jobs_by_search_terms(jobs_search_terms)

	visualize_data_in_bar_chart(jobs_search_terms, jobs_count, chart_title)

if type_of_jobs == 'remote':
	if site_to_get_data_from == 'linkedin':
		jobs_count = get_remote_linkedin_jobs_by_search_terms(jobs_search_terms)
	if site_to_get_data_from == 'indeed':
		jobs_count = get_indeed_jobs_by_search_terms(jobs_search_terms, 'remote')

	visualize_data_in_bar_chart(jobs_search_terms, jobs_count, chart_title)

if type_of_jobs == 'both':
	if site_to_get_data_from == 'linkedin':
		on_site_jobs_count = get_on_site_linkedin_jobs_by_search_terms(jobs_search_terms)
		remote_jobs_count = get_remote_linkedin_jobs_by_search_terms(jobs_search_terms)

	if site_to_get_data_from == 'indeed':
		on_site_jobs_count = get_indeed_jobs_by_search_terms(jobs_search_terms)
		remote_jobs_count = get_indeed_jobs_by_search_terms(jobs_search_terms, 'remote')
	
	visualize_data_in_grouped_bar_chart(jobs_search_terms, on_site_jobs_count, remote_jobs_count, chart_title)
