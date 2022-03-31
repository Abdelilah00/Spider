import requests

import dataCollector

requests.post('http://localhost:8080/collector', json=dataCollector.collect())