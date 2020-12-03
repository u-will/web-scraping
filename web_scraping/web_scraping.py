import requests
from bs4 import BeautifulSoup

def get_citation_needed_count(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  count_ell = soup.find_all('a', title='Wikipedia:Citation needed')
  return len(count_ell)

count  = get_citation_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico')


def get_citation_needed_report(url):
  count = get_citation_needed_count(url)
  print(f"there are {count} numbers of citation needed")