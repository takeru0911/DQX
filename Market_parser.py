from BeautifulSoup import BeautifulSoup
from BeautifulSoup import NavigableString
import requests
import simplejson as json
scraping_data = []
for i in range(12) :
    url = "http://grooowl.com/r/dqx/alchemy_recipe/top/1/1/0/0/" + str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    trTags = soup.findAll('tr')
 
    for trTag in trTags :
        tdTag = trTag.findAll('td')
        for items in trTag :
            if not isinstance(items, NavigableString) :
                item = items.findAll('div')
                if len(item) != 0 :
                    if len(item) > 1 :
                        detailOfItem = item[0].find('a')
                        kindOfItem = item[1].find('a')
                        if (not detailOfItem is None) and (not kindOfItem is None) :
                            
     
                            item_url = detailOfItem['href']
                            item_name = detailOfItem.string
                            item_id = item_url.replace('/r/dqx/bazaar_list_histories/detail/', '')
                            kind_url = kindOfItem['href']
                            kind_name = kindOfItem.string
                            kind_id = kind_url.replace('/r/dqx/bazaar_list/top/', '')
                            item_id = item_id
                            data = {
                                "id": item_id,
                                "item_name": item_name,
                                "item_url": item_url,
                                "kind_id": kind_id,
                                "kind_name": kind_name,
                                "kind_url": kind_url
                            }
                            scraping_data.append(data)
     
     
temp = json.dumps(scraping_data, ensure_ascii=False, indent=2)
print temp



                        

                        

