import json
import requests
from bs4 import BeautifulSoup
from config import BASE_DIR
import time



def get_jobs():
	s = requests.Session()
	
	html = s.get("https://www.weblancer.net/jobs/veb-programmirovanie-31/").text
	soup = BeautifulSoup (html, 'html.parser')
	web_containers = soup.find_all("div", class_="row click_container-link set_href")
	
	time.sleep(5)

	html = s.get("https://www.weblancer.net/jobs/prikladnoe-po-23/").text
	soup = BeautifulSoup (html, 'html.parser')
	po_containers = soup.find_all("div", class_="row click_container-link set_href")
	
	new_jobs = {}
	for container in web_containers:
		row = container.find("a", class_="text-bold click_target show_visited")
		new_jobs[row.text] = "https://www.weblancer.net" + row.attrs["href"]

	for container in po_containers:
		row = container.find("a", class_="text-bold click_target show_visited")
		new_jobs[row.text] = "https://www.weblancer.net" + row.attrs["href"]

	jobs = new_jobs.copy()
	new_jobs = set(new_jobs.keys())

	with open(BASE_DIR / 'jobs.json') as json_file:
	    old_jobs = set(json.load(json_file))

	set.difference_update(new_jobs, old_jobs)
	new_jobs = list(new_jobs)

	with open(BASE_DIR / 'jobs.json', 'w') as outfile:
	    json.dump(list(jobs.keys()), outfile)
	data = {}
	for title in new_jobs:
		data[title] = jobs[title]
	return data