from parser import get_jobs
from config import API_KEY, CHANNEL_ID
import requests


jobs = get_jobs()
if jobs:
	text = ""
	for key, val in jobs.items():
		text += f"[{key}]({val})\n"
	url = f"https://api.telegram.org/bot{API_KEY}/sendMessage"
	data = {"chat_id": CHANNEL_ID, "text": text, "parse_mode": "Markdown"}
	response = requests.post(url, data=data)