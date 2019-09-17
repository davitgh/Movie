#!/usr/bin/python3.4

import requests
from bs4 import BeautifulSoup

#url = 'https://filmix.co/'

def get_movie_details(url):
	#  download page
	page = requests.get(url)

	# Create a BeautifulSoup object
	soup = BeautifulSoup(page.text, 'html.parser')
	#print(soup)
	films_container = soup.find('div', {'id': 'dle-content'})
	# Find article
	articles = films_container.find_all('article')
	for article in articles:
		img = article.find('a', href=True)
		thumb = article.find('img')
		print('{')
		print("   img : " + img['href'])
		print("   thumbnail : " + thumb['src'])

		name = article.find('a', class_='btn-tooltip')
		orig_name = article.find('div', class_="origin-name")
		print("   name : " + name['title'])
		print("   page : " + name['href'])
		print("   orig_name : " + orig_name['content'])
		print('},')


pages = 4545

for page_i in range(1, pages):
	if page_i == 1:
		get_movie_details('https://filmix.co/')
	else:
		get_movie_details("https://filmix.co/page/" + str(page_i) )
