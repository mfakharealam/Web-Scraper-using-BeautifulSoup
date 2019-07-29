from bs4 import BeautifulSoup
import requests
import csv

html_source = requests.get('https://coreyms.com').text
soup = BeautifulSoup(html_source, 'lxml')
csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Post Headline', 'Post Summary', 'YouTube Link'])  # setting headers for the file, col names

# print(soup.prettify())
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)
    content_div = soup.find('div', class_='entry-content')
    content = content_div.p.text
    print(content)
    try:
        video_src = article.find('iframe', 'youtube-player')['src']  # stored like a dictionary
        video_id = video_src.split('/')[4]
        video_id = video_id.split('?')[0]

        # creating a youtube link
        yt_link = f'https://youtube.com/watch?v={video_id}'
    except Exception as E:
        yt_link = None
    print(yt_link)
    print()     # empty line
    #  writing to csv file
    csv_writer.writerow([headline, content, yt_link])

csv_file.close()
