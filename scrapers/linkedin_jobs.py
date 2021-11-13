from scrapers.linkedin_jobs_all import get_all_linkedin_jobs_by_search_terms
from scrapers.linkedin_jobs_remote import get_remote_linkedin_jobs_by_search_terms

# Create one function for both on site and remote jobs so we can call them dynamically with the function name
def get_linkedin_jobs_by_search_terms(jobs_search_terms, all_or_remote_jobs):
	if all_or_remote_jobs == 'all':
		return get_all_linkedin_jobs_by_search_terms(jobs_search_terms)

	if all_or_remote_jobs == 'remote':
		return get_remote_linkedin_jobs_by_search_terms(jobs_search_terms)

	print('Bad input, please select either "all" or "remote" without the quotes! Exiting from the program!')
	exit()
