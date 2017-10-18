import urllib.request
import json
import sys


def send_tocaro(url_id,title,message):
	args = sys.argv
	url = "https://hooks.tocaro.im/integrations/inbound_webhook/" + url_id

	method = "POST"
	headers = {"Content-Type" : "application/json"}

	obj = { "text": "Delayed NBU-JOB info nortice. from take-script.", "color": "info", "attachments": [{"title": title, "value": message}, {}] }
	json_data = json.dumps(obj).encode("utf-8")

	request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
	with urllib.request.urlopen(request) as response:
		response_body = response.read().decode("utf-8")
