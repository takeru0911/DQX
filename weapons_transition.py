#coding:utf-8AOA
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import NavigableString
import requests
import simplejson as json
import os



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
levels = [
    '1',
    '31'
]
kinds = [
    '1', 
    '2', 
    '3', 
    '4', 
    '5', 
    '8' 
]    

#for kind in kinds :
#    for level in levels :    
#    e
for level in levels :
    for kind in kinds :
        f = open("/vagrant/" + kind +"_" + level + ".json", 'r')
        s = f.read()
        f.close()
        items = json.loads(s)
        marker = ''
        s_0 = {'exhibits' : '', 'price': ''} 
        s_1 = {'exhibits' : '', 'price': ''} 
        s_2 = {'exhibits' : '', 'price': ''} 
        s_3 = {'exhibits' : '', 'price': ''} 
         
        for item in items :
            id = item['id']
            print item['item_name']
            os.mkdir("/vagrant/" + str(id))
         
            for month in date :
                scraping_data = []
                print month
                for i in range(0, 4) :
                    url = "http://grooowl.com/r/dqx/bazaar_list_histories/history2/"+ str(id) + "/" + month + "/" + str(i)
                    print url
                    r = requests.get(url)
         
                    soup = BeautifulSoup(r.text)
                 
                     
                    time = ''
                     
                    trTags = soup.findAll('tr')
                     
                    k = 0
                    for trTag in trTags :
                        k = k + 1
                        tdTags = trTag.findAll('td')
                        exhibits = ''
                        price = ''
         
                        
                     
                        for tdTag in tdTags :
                            if tdTag.get('class') == 'lh1':
                                if time != '' :
                                    print "1"
                                    data = {
                                        'id': id,
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
                                    exhibits = ''
                                    price = ''
                                    scraping_data.append(data)
                                    
                                planeText = tdTag.text
                                time = planeText.split(u'（')[1].split(u'）')[0]
                            elif tdTag.get('class') == 'n2':
                                if not tdTag.find('span') is None :
                                    stars = tdTag.find('span').string
         
                                    if stars == '★':
                                        marker = '2'
                                    elif stars == '★★' :
                                        marker = '1'
                                    elif stars == '★★★':
                                        marker = '0'
         
                                else :
                                    if tdTag.string == '★★★':
                                        marker = '3'
                                    
                                
                                plane = tdTag.string
                
         
                            elif tdTag.get('class') == 'n d1 m ' or tdTag.get('class') == 'n d1  ':
                                price = tdTag.text.replace('G', '')
             
                            elif tdTag.get('class') == 'n ' or tdTag.get('class') == 'n r':
                                exhibits = tdTag.text.replace('件', '')
        #                    print marker + ",pr, " + price
        #                    print marker + ",ex, " + exhibits
                            
             
                        
                            if   s_0['exhibits'] == '' and exhibits != '' and marker == '0':
                                s_0['exhibits'] = exhibits                                 
                                exhibits = ''
                                marker = ''
                            elif s_1['exhibits'] == '' and exhibits != '' and marker == '1':
                                s_1['exhibits'] = exhibits                                 
                                exhibits = ''
                                marker = ''
                            elif s_2['exhibits'] == '' and exhibits != '' and marker == '2':
                                s_2['exhibits'] = exhibits                                 
                                exhibits = ''
                                marker = ''
                            elif s_3['exhibits'] == '' and exhibits != '' and marker == '3':
                                s_3['exhibits'] = exhibits
                                exhibits = ''
                                marker = ''
                            if   s_0['price'] == '' and price != ''and marker == '0':
                                s_0['price'] = price                                
                                price = ''
                            elif s_1['price'] == '' and price != ''and marker == '1':
                                s_1['price'] = price
                                price = ''                                          
                            elif s_2['price'] == '' and price != ''and marker == '2':
                                s_2['price'] = price                                
                                price = ''                                          
                            elif s_3['price'] == '' and price != ''and marker == '3':
                                s_3['price'] = price
                                price = ''
                             
         
                       
                
                    if time != '' :
                        data = {
                            'id': id,
                            'time' : time,
                            'star0': s_0,
                            'star1': s_1,
                            'star2': s_2,
                            'star3': s_3
                        }
                        scraping_data.append(data)
                        s_0 = {'exhibits' : '', 'price': ''} 
                        s_1 = {'exhibits' : '', 'price': ''} 
                        s_2 = {'exhibits' : '', 'price': ''} 
                        s_3 = {'exhibits' : '', 'price': ''}
                        exhibits = ''
                        price = ''
         
         
                temp = json.dumps(scraping_data, ensure_ascii=False, indent=2)
                #        f = open("/vagrant/te.json", 'w')
        #        print temp
                f = open("/vagrant/" + str(id) + "/" + month + ".json", 'w')
                f.write(temp.encode('utf-8'))
                f.close();
                scraping_data = []
                s_0 = {'exhibits' : '', 'price': ''} 
                s_1 = {'exhibits' : '', 'price': ''} 
                s_2 = {'exhibits' : '', 'price': ''} 
                s_3 = {'exhibits' : '', 'price': ''}
                exhibits = ''
                price = ''
         

