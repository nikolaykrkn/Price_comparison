from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import time
from decimal import *

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) '
			'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
			}


def get_price(URL):
	error_count = 0
	while True:
		try:
			req = Request(URL, data=None, headers=HEADERS)

			with urlopen(req) as site:
				soup = BeautifulSoup(site.read().decode('utf-8'), 'html.parser')
				break
		except:
			time.sleep(5)
			error_count += 1
			if error_count < 5:
				return -2.0

	if "www.prodirectrunning.com" in URL or "www.wiggle.co.uk" in URL:
		return soup.select("[itemprop='price']")[0].text
	elif "www.activeinstyle.com" in URL:
		return str(soup.select("[itemprop='price']")[0]).split('meta content="', 1)[1].split('"', 1)[0]

if __name__ == "__main__":
	URL = "http://www.prodirectrunning.com/products/2XU-Compression-Long-Sleeve-Top-Black-Silver-X-Mens-Base-Layer-MA2308aBlack-Silver-X-147587.aspx?spr=1"
	p = get_price(URL)
	print(p)