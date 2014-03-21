"""
When passing in the url as an argument, note they are indexed by & symbols b/c
you cannot send a command line argument with the & symbol.
"""

from xml.dom import minidom
from os import sys
import urllib.requeprint((sys.argv))
fi = open('meetupData.txt', 'r')
url = ''
url = fi.readline()[:-2]
page = urllib.request.urlopen(url)
f = open('xmlFile.xml', 'w')
o = open('meetupData.txt', 'w')
a = str(page.read())
f.write(a[46:-3])
f.close()
xmldoc = minidom.parse('xmlFile.xml')
itemlist = xmldoc.getElementsByTagName('name') 
print (len(itemlist))
#print (itemlist[0].attributes['name'].value)
for s in itemlist :
    o.write(s.firstChild.data + "\n")
o.close()
   
