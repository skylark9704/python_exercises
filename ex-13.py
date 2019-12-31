# Ex-15
# Use urllib2 module to get html content from this link:
# http://www.mattmakai.com/links-learning-web-fundamentals.html
# Python has beautifulsoup library to parse html.
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/
# Print all anchor tags, exclude relative links

import urllib2
import re
from bs4 import BeautifulSoup

response = urllib2.urlopen("http://www.mattmakai.com/links-learning-web-fundamentals.html")

html = response.read()

parsed = BeautifulSoup(html, 'html.parser')

anchors = re.findall("^<a>", html)

print(parsed.prettify())


