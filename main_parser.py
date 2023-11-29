import requests
from bs4 import BeautifulSoup as bs

URL_TEMPLATE = "https://olimpiada.ru/news"
r = requests.get(URL_TEMPLATE)
soup = bs(r.text, "html.parser")
def get_physic(soup=soup):
    ans = []
    physic = soup.find_all('span', class_='icon-physics')
    for i in physic:
        ans.append(str(i.parent.parent.parent.a.contents[0]) + '\n')
    return ans
def get_math(soup=soup):
    ans = []
    math = soup.find_all('span', class_='icon-math')
    for i in math:
        ans.append(str(i.parent.parent.parent.a.contents[0]) + '\n')
    return ans
def get_informatics(soup=soup):
    ans = []
    informatics = soup.find_all('span', class_='icon-informatics')
    for i in informatics:
        ans.append(str(i.parent.parent.parent.a.contents[0]) + '\n')
    return ans
phys = get_physic()
math = get_math()
inf = get_informatics()
