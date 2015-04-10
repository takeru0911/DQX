#coding:utf-8
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import NavigableString
import requests
import simplejson as json


f = open('2014-12')
html = f.read()
f.close()

date = [
    '2013-03',
    '2013-04',
    '2013-05',
    '2013-06',
    '2013-07',
    '2013-08',
    '2013-09',
    '2013-10',
    '2013-11',
    '2013-12',
    '2014-01',
    '2014-02',
    '2014-03',
    '2014-04',
    '2014-05',
    '2014-06',
    '2014-07',
    '2014-08',
    '2014-09',
    '2014-10',
    '2014-11',
    '2014-12',
    '2015-01',
    '2015-02',
    '2015-03',
    '2015-04'

]
for month in date :
    scraping_data = []
    print month
    for i in range(0, 4) :
        url = "http://grooowl.com/r/dqx/bazaar_list_histories/history2/631/" + month + "/" + str(i)
#        print url
        r = requests.get(url)
#        print r.text
        soup = BeautifulSoup(r.text)
     
         
        time = ''
        exhibits = ''
        price = ''
         
        trTags = soup.findAll('tr')
        s_0 = {'exhibits' : '', 'price': ''} 
        s_1 = {'exhibits' : '', 'price': ''} 
        s_2 = {'exhibits' : '', 'price': ''} 
        s_3 = {'exhibits' : '', 'price': ''} 
         
        k = 0
        for trTag in trTags :
            k = k + 1
            tdTags = trTag.findAll('td')
         
            for tdTag in tdTags :
                if tdTag.get('class') == 'lh1':
                    if time != '' :
                        data = {
                            'id': '0',
                            'time' : time,
                            'star0': s_0,
                            'star1': s_1,
                            'star2': s_2,
                            'star3': s_3
                            }
                        s_0 = {'exhibits' : '', 'price': ''} 
                        s_1 = {'exhibits' : '', 'price': ''} 
                        s_2 = {'exhibits' : '', 'price': ''} 
                        s_3 = {'exhibits' : '', 'price': ''} 
         
                        scraping_data.append(data)
                    planeText = tdTag.text
                    time = planeText.split(u'（')[1].split(u'）')[0]
                elif tdTag.get('class') == 'n2':
                    plane = tdTag.string
                    if not plane is None :
                        temp = plane.split(' 件')[0]
                        if temp.isdigit() :
                            exhibits = temp
                elif tdTag.get('class') == 'n d1 m ' or tdTag.get('class') == 'n d1  ':
                    price = tdTag.text.replace('G', '')
                    
            if s_0['exhibits'] == '' and exhibits != '':
                s_0['exhibits'] = exhibits
                exhibits = ''
            elif s_1['exhibits'] == '' and exhibits != '':
                s_1['exhibits'] = exhibits
                exhibits = ''
            elif s_2['exhibits'] == '' and exhibits != '':
                s_2['exhibits'] = exhibits
                exhibits = ''
            elif s_3['exhibits'] == '' and exhibits != '':
                s_3['exhibits'] = exhibits
                exhibits = ''
         
            if s_0['price'] == '' and price != '':
                s_0['price'] = price
                price = ''
            elif s_1['price'] == '' and price != '':
                s_1['price'] = price
                price = ''
            elif s_2['price'] == '' and price != '':
                s_2['price'] = price
                price = ''
            elif s_3['price'] == '' and price != '':
                s_3['price'] = price
                price = ''
        if time != '' :
            data = {
                'id': '0',
                'time' : time,
                'star0': s_0,
                'star1': s_1,
                'star2': s_2,
                'star3': s_3
                }
            scraping_data.append(data)    
    temp = json.dumps(scraping_data, ensure_ascii=False, indent=2)
    f = open("/vagrant/sample-" + month + ".json", 'w')
    f.write(temp.encode('utf-8'))
    f.close();

     
        
     

