# My attempt at a Python Web Scraper for Newegg.com VR Headsets currently being sold

# Adapted from a YouTube tutorial (Data Science Dojo)
# By Chris Huffman 2017

from urllib.request import urlopen as uReq #allows accessing of internet 
from bs4 import BeautifulSoup as soup  

my_url = 'https://www.newegg.com/VR-Headsets/SubCategory/ID-3629'

# opening up connection and grabbing page
uClient = uReq(my_url)
vr_page = uClient.read()
uClient.close()

# html parser
vr_soup = soup(vr_page, "html.parser")

# grabs each VR headset and their information
containers = vr_soup.findAll("div", {"class":"item-container"})

# find all results on page with a loop
for container in containers:
	model_container = container.findAll("a", {"class":"item-title"})
	make = model_container[0].text.split(' ',1)[0]
	model = model_container[0].text
	print ("Make: " + make)
	print ("Model: " + model)