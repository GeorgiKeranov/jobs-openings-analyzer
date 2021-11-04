import time
import urllib.parse
from bs4 import BeautifulSoup
from urllib.request import urlopen
from visualize_data import visualize_data_in_pie_chart

programming_technologies = [
	"JavaScript Developer",
	"Java Developer",
	"Python Developer",
	"Swift Developer",
	"Perl Developer",
	"Rust Developer",
	"C# Developer",
	"SQL Developer",
	"C++ Developer",
	"C Developer",
	"Golang Developer",
	"PHP Developer",
	"Ruby Developer",
];

tech_jobs_count = [];

url = "https://www.indeed.com/jobs?";

# Filter only by the remote jobs
# url = url + 'remotejob=032b3046-06a3-4876-8dfd-474eb5e7ed11&'

for tech in programming_technologies:
	url_specific = url + 'q=' + urllib.parse.quote(tech);

	page = urlopen(url_specific)
	html = page.read().decode("utf-8")
	soup = BeautifulSoup(html, "html.parser")

	jobs_count_text = soup.find("div", {"id" : "searchCountPages"}).text
	jobs_count_text = ((jobs_count_text.split("of "))[1]).split(" jobs")[0]
	jobs_count = jobs_count_text.replace(",", "")
	jobs_count = int(jobs_count)

	tech_jobs_count.append(jobs_count);

	time.sleep(2)

print(tech_jobs_count)
print(programming_technologies)

visualize_data_in_pie_chart(tech_jobs_count, programming_technologies)
