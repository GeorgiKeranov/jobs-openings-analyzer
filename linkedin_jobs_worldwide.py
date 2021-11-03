import time
import urllib.parse
from bs4 import BeautifulSoup
from urllib.request import urlopen


programming_technologies = [
	"Spring Boot",
	"Express.js",
	"Django",
	"Ruby on Rails",
	"Laravel",
];

tech_jobs_count = [];

url = "https://www.linkedin.com/jobs/search?location=Worldwide&geoId=92000000&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0&keywords=";

for tech in programming_technologies:
	url_specific = url + urllib.parse.quote(tech);

	page = urlopen(url_specific)
	html = page.read().decode("utf-8")
	soup = BeautifulSoup(html, "html.parser")

	jobs_count_text = soup.find("label", {"for" : "f_TPR-3"}).text
	jobs_count_text = ((jobs_count_text.split("("))[1]).split(")")[0]
	jobs_count = jobs_count_text.replace(",", "")
	jobs_count = int(jobs_count)

	tech_jobs_count.append(jobs_count);

	time.sleep(2)


print(tech_jobs_count)
print(programming_technologies)

