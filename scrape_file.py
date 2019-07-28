from bs4 import BeautifulSoup
import requests

with open('sample.html') as html_file:
    bsoup = BeautifulSoup(html_file, 'lxml')

# print(bsoup.prettify())  # indents the code

# match = bsoup.title.text  # only returns the first tag relevant to 'title'
# print(match)

# using find method to find exact tag you want

match = bsoup.find('div', class_='footer') # using class_ to differentiate b/w python's class and bs

