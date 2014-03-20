import urllib.request
page = urllib.request.urlopen('https://api.meetup.com/2/open_events.xml?topic=photo&key=346f4a513547d677934427478787649')
f = open('xmlFile.xml', 'w')
a = str(page.read())
