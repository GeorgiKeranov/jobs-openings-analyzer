import helpers.main_helper as helper
from helpers.visualize_data import visualize_data_in_grouped_bar_chart
from helpers.visualize_data import visualize_data_in_bar_chart
from scrapers.indeed_jobs import get_indeed_jobs_by_search_terms
from scrapers.linkedin_jobs import get_linkedin_jobs_by_search_terms

type_of_jobs_options = ['on_site', 'remote', 'both']
type_of_jobs_selected = helper.get_console_option('Which type job jobs you want?', type_of_jobs_options)

site_options = [ 'linkedin', 'indeed' ]
site_selected = helper.get_console_option('Which site you want to get data from?', site_options)

print('\nPlease wait, it may take a while to scrape all the data from the site\n')

# Get all jobs search terms in 'jobs_search_terms.txt' file and convert them into array
jobs_search_terms = helper.get_search_terms_from_file('jobs_search_terms.txt')

chart_title = helper.generate_chart_title(site_selected, type_of_jobs_selected)

# Generate function name based on the site selected
# Example 1 - site selected is 'indeed' so generate "get_indeed_jobs_by_search_terms"
# Example 2 - site selected is 'linkedin' so generate "get_linkedin_jobs_by_search_terms"
function_name = helper.generate_function_name(site_selected)

# Get both on-site and remote jobs in one chart
if type_of_jobs_selected == 'both':
	# Call function with 'function_name' dynamically
	on_site_jobs_count = globals()[function_name](jobs_search_terms, 'on_site')
	remote_jobs_count = globals()[function_name](jobs_search_terms, 'remote')

	visualize_data_in_grouped_bar_chart(jobs_search_terms, on_site_jobs_count, remote_jobs_count, chart_title)
else:
	jobs_count = globals()[function_name](jobs_search_terms, type_of_jobs_selected)

	visualize_data_in_bar_chart(jobs_search_terms, jobs_count, chart_title)
