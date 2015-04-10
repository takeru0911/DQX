from BeautifulSoup import BeautifulSoup
from BeautifulSoup import NavigableString
import requests
import simplejson as json


scraping_data = []

for i  in range(0, 2) :

    url = "http://grooowl.com/r/dqx/alchemy_recipe/top2/6/1/0/0/0/" + str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text)

    trTags = soup.findAll('tr')
    materials = []

    for trTag in trTags :
        data = []
        tdTag = trTag.findAll('td')
     
        if not isinstance(tdTag, NavigableString) :
            for items in tdTag :
         
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
                                    "kind_url": kind_url,
                                    "materials": []
                                    
                                }
                                scraping_data.append(data)
                                
                    if items.get('class') == 'recipe_material_nm nm s' :
                        strHTML =  items.prettify()
                        strHTMLs = strHTML.split('</a>')
                        temp =  strHTMLs[1]
                        numOfrequire = temp.replace("\n</td>\n", '').replace("\nx", '')
     
                        materialRaw = items.find('a')
                        material_url = materialRaw['href']
                        material_name = materialRaw.string
                        material_id = material_url.replace('/r/dqx/bazaar_list_histories/detail/', '')
                        material_require = numOfrequire
                        material = {
                            "material_id": material_id,
                            "material_name": material_name,
                            "material_url": material_url,
                            "material_require": material_require
                            }
                        scraping_data[len(scraping_data) - 1]["materials"].append(material)
     
     
    #                    materials.append(material)
     
     
     
     
     
    #    if data != [] :
    #        print materials
    #        data["materials"] = materials
    #        materials = []
                                


temp = json.dumps(scraping_data, ensure_ascii=False, indent=2)
print temp.encode('utf-8')
