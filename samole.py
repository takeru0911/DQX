#coding:utf-8
import simplejson as json
import os

os.mkdir('/vagrant/test')
f = open('/vagrant/weapon_1to30.json', 'r')
s = f.read()
f.close()
items = json.loads(s)

for item in items :
    print item['item_name']
