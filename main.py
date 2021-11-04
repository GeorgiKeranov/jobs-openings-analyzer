from scrapers.indeed_jobs import get_indeed_jobs_by_search_terms
from scrapers.linkedin_jobs_on_site import get_on_site_linkedin_jobs_by_search_terms
from scrapers.linkedin_jobs_remote import get_remote_linkedin_jobs_by_search_terms
from helpers.visualize_data import visualize_data_in_pie_chart

# Here you can change the search terms to the things you want
# to analyze like for example progamming languages, frameworks, etc.
jobs_search_terms = [
	"Python Developer",
	"JavaScript Developer",
	"Java Developer",
	"C# Developer",
	"C++ Developer",
	"C Developer",
	"PHP Developer",
	"Ruby Developer",
	"Golang Developer",
	"Swift Developer",
];

# indeed_on_site_jobs_count = get_indeed_jobs_by_search_terms(jobs_search_terms)
# indeed_remote_jobs_count = get_indeed_jobs_by_search_terms(jobs_search_terms, 'remote')
# linkedin_on_site_jobs_count = get_on_site_linkedin_jobs_by_search_terms(jobs_search_terms)
# linkedin_jobs_remote = get_remote_linkedin_jobs_by_search_terms(jobs_search_terms)

# visualize_data_in_pie_chart()
