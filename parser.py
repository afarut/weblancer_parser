import json
import requests
from bs4 import BeautifulSoup
from config import BASE_DIR

def get_jobs():
	s = requests.Session()
	html = s.get("https://www.weblancer.net/jobs/veb-programmirovanie-31/").text
	soup = BeautifulSoup (html, 'html.parser')
	containers = soup.find_all("div", class_="row click_container-link set_href")
	new_jobs = set(map(lambda x: x.find("a", class_="text-bold click_target show_visited").text, containers))
	jobs = list(new_jobs.copy())

	with open(BASE_DIR / 'jobs.json') as json_file:
	    old_jobs = set(json.load(json_file))

	set.difference_update(new_jobs, old_jobs)
	new_jobs = list(new_jobs)

	with open(BASE_DIR / 'jobs.json', 'w') as outfile:
	    json.dump(jobs, outfile)
	return new_jobs