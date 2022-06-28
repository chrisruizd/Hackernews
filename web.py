#Cleaning up Hacker news

import imp
import requests # allows you to download the html
from bs4 import BeautifulSoup   #allows you to use the datat and scrape the datat on the html
import pprint   #used to print things more organized 'pretty print'

#notice that you can add more page news just by increasing news?p=3...
#to optimize use a function
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.titlelink') #heads up! .storylink changed to .titlelink
subtext = soup.select('.subtext')
links2 = soup2.select('.titlelink') #heads up! .storylink changed to .titlelink
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

#this func creates a list of dict that stores the info of every news with only the ones 100 votes or more
def create_custom_hn(links, subtext):   #you always will have a link but not always a vote or subtext
  hn = []
  for idx, item in enumerate(links):    #notice only looping 'links' enumerate is used to keep the index and usint for 'subtext'
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99:
        hn.append({'title': title, 'link': href, 'votes': points})
  return sort_stories_by_votes(hn)
 
pprint.pprint(create_custom_hn(mega_links, mega_subtext))
