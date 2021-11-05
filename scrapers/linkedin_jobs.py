from scrapers.linkedin_jobs_on_site import get_on_site_linkedin_jobs_by_search_terms
from scrapers.linkedin_jobs_remote import get_remote_linkedin_jobs_by_search_terms

def get_linkedin_jobs_by_search_terms(jobs_search_terms, on_site_or_remote_jobs):
	if on_site_or_remote_jobs == 'on_site':
		return get_on_site_linkedin_jobs_by_search_terms(jobs_search_terms)

	if on_site_or_remote_jobs == 'remote':
		return get_remote_linkedin_jobs_by_search_terms(jobs_search_terms)

	print('Bad input, please select either "on_site" or "remote" without the quotes! Exiting from the program!')
	exit()
