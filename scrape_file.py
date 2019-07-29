from bs4 import BeautifulSoup
import requests

html_source = requests.get('https://coreyms.com').text
soup = BeautifulSoup(html_source, 'lxml')
# print(soup.prettify())
article = soup.find('article')
# headline = article.h2.a.text
# print(headline)
# content_div = soup.find('div', class_='entry-content')
# content = content_div.p.text
# print(content)
video_src = article.find('iframe', 'youtube-player')['src']  # stored like a dictionary
video_id = video_src.split('/')[4]
video_id = video_id.split('?')[0]
print(video_id)
