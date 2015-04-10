#coding:utf-8
import simplejson as json

f = open('/vagrant/weapon_1to30.json', 'r')
s = f.read()
f.close()
print json.loads(s)
