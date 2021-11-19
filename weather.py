from prometheus_client import start_http_server, Summary, Gauge
import random
import time
import requests
import xml.etree.ElementTree as ET
from datetime import datetime

# Create a metric
g = Gauge('tallinn_temperature', 'Air temperature in Tallinn')


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Fetch weather
    while True:
        url = "http://www.ilmateenistus.ee/ilma_andmed/xml/observations.php"
        response = requests.get(url)
        root = ET.fromstring(response.content)
        for t in root.findall('station'):
            name = t.find('name').text
            at = t.find('airtemperature').text
            if name == 'Tallinn-Harku':
                g.set(at)
        time.sleep(60)
