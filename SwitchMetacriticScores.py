import requests

def getnextpage(soup):
    page = soup.find()
    if not page.find('',{}):

from bs4 import BeautifulSoup
user_agent = {'User-agent': 'Mozilla/5.0'}
url = 'https://www.metacritic.com/search/all/nintendo%20switch/results'
page = requests.get(url, headers = user_agent)
soup = BeautifulSoup(page.content, 'html.parser')
page_head = soup.heads
all_grades = {'good':[], 'mediocre':[],'bad':[]}
divs = soup.find_all('li', class_= 'result')
for grade in divs:
    if grade.find('span', class_='metascore_w medium game positive'):
        all_grades['good'].append(grade.find('span', class_='metascore_w medium game positive').text)
    elif grade.find('span', class_='metascore_w medium game mixed'):
        all_grades['mediocre'].append(grade.find('span', class_='metascore_w medium game mixed').text)
    elif grade.find('span', class_='metascore_w medium game negative'):
        all_grades['bad'].append(grade.find('span', class_='metascore_w medium game negative').text)
print("Total number of highly rated games: ", len(all_grades.get("good")))
print("Total number of mixed rated games: ", len(all_grades.get("mediocre")))
print("Total number of horribly rated games: ", len(all_grades.get("bad")))