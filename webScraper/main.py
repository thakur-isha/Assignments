from bs4 import BeautifulSoup
import requests

class webCrawler:
  def __init__(self,url):
    self.url = url
  def getData(self):
    '''
    This function will crawl on the website's url whose data we want to fetch
    :param url: url of the website from which we want to fetch information
    :return: return data from the first page of url in a sorted way
    '''
    request = requests.post(self.url)

    soup = BeautifulSoup(request.content,'lxml')
    title = soup.find_all("a",{"class": "titlelink"})
    rank = soup.find_all("span",{"class": "rank"})
    raw_data = soup.find_all('td',{'class':'subtext'})
    data = []
    comments = []
    points = []
    # A few news post does not have comments and points so iterating the data to set the same data
    for c in raw_data:
      if 'comment' in c.text:
        comments.append(int(c.text.split('|')[-1].strip(' comment').strip(' comments')))
      else:
        comments.append(0)
      if 'point' in c.text:
        points.append(int(c.text.split('point')[0]))
      else:
        points.append(0)

    for x in range(0, len(title)):
      data.append({'title':title[x].text.strip(),'points':points[x],
                   'rank':rank[x].text.strip('.'),'comments':comments[x]})

    return data

  def filterOperation(self,data):
    data_grter_than_five = []
    data_less_than_or_eq_to_five = []
    newlist = dict()

    for d in data:
      title = d['title']
      if len(title.split()) > 5:
        data_grter_than_five.append(d)
      else:
        data_less_than_or_eq_to_five.append(d)

    if data_grter_than_five:
      newlist['data_grter_than_five'] = sorted(data_grter_than_five,  key=lambda x: int(x['comments']), reverse=True)
    if data_less_than_or_eq_to_five:
      newlist['data_less_than_or_eq_to_five'] = sorted(data_less_than_or_eq_to_five, key=lambda x: int(x['points']))

    return newlist

url = 'https://news.ycombinator.com/'
web = webCrawler(url)
data = web.getData()
# filter the data if count is more than 5 words then sort by number of comments
# and if count is less than 5 words then sort by number of comments
filter_data = web.filterOperation(data)
print(filter_data)

