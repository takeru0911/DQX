from BeautifulSoup import BeautifulSoup
from BeautifulSoup import NavigableString
import requests
import simplejson as json



scraping_data = []

for i in range(0, 7) :
    url = "http://grooowl.com/r/dqx/bazaar_list/top/901/0/0/" + str(i)
    r = requests.get(url)
    
    soup = BeautifulSoup(r.text)
    trTags = soup.findAll('tr')
    for trTag in trTags :
        tdTags = trTag.findAll('td')
        for tdTag in tdTags :
            if tdTag.get('class') == 'nm lh1' :
                material = tdTag.find('table').find('tr').find('td').find('a')
                material_url = material['href']
                material_name = material.string
                material_id = material_url.replace('/r/dqx/bazaar_list_histories/detail/', '')
                material = {
                    "id": material_id,
                    "material_name": material_name,
                    "material_url": material_url
                    }
                scraping_data.append(material)
temp = json.dumps(scraping_data, ensure_ascii=False, indent=2)
print temp.encode('utf-8')


            





