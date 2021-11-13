# Get all lines from text file as array
def get_search_terms_from_file(file_name):
	with open(file_name) as jobs_search_terms_file:
		jobs_search_terms = [line.strip() for line in jobs_search_terms_file.readlines()]

	if not jobs_search_terms:
		print('Please add all of the search terms that you want to search by in "jobs_search_terms.txt" file in the main directory.\n')
		print('Please note that each term have to be on new line.')
		exit()

	return jobs_search_terms

# Print question and options in console and give the user to choose option
def get_console_option(question, options):
	print('\n' + question + ' You have these options to choose from:')

	for option in options:
		print('    - ' + option)

	option_selected = input('Select one of the above options: ').lower()

	if option_selected not in options:
		print('\nERROR: Incorrect option selected, please check the options again')
		exit()

	return option_selected

# Generates chart tile based on the selected site and the type of jobs
def generate_chart_title(site_selected, type_of_jobs_selected):
	chart_title = 'Job Openings'

	if type_of_jobs_selected != 'both':
		chart_title = type_of_jobs_selected.replace('_', ' ').capitalize() + ' ' + chart_title

	if site_selected != 'all':
		chart_title += ' in ' + site_selected.capitalize()

	return chart_title

# Generate dynamic function name based on the site selected
def generate_function_name(site_selected):
	function_name = 'get_' + site_selected + '_jobs_by_search_terms'

	return function_name
