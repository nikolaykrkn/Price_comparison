from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import time
from decimal import *
import codecs

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) '
			'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
			}


def get_price(URL):
	error_count = 0
	#while True:
	#	try:
	req = Request(URL, data=None, headers=HEADERS)

	with urlopen(req) as site:
				soup = BeautifulSoup(site.read().decode('utf-8'), 'html.parser')
	#			break
	#	except:
	#		time.sleep(5)
	#		error_count += 1
	#		if error_count < 5:
	#			return -2.0
	htmlfile = 'check.html'
	with open(htmlfile, 'wb') as output:
		file = codecs.encode(str(soup), 'utf-8')
		output.write(file)

	if "prodirectrunning.com" in URL or "wiggle.co.uk" in URL:
		return soup.select("[itemprop='price']")[0].text
	elif "www.activeinstyle.com" in URL or "thesportsedit.com" in URL or "hipandhealthy.com" in URL or "yogarebel.com" in URL:
		prc_tags = soup.find(attrs={'itemprop':'price'})
		return prc_tags['content']

if __name__ == "__main__":
	URL = "https://thesportsedit.com/products/2xu-compression-long-sleeves-top"
	p = get_price(URL)
	print(p)