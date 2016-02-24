#Python 3.4
#2.7                         3.4
#urllib2                     urllib
#urllib.urlopen      urllib.request.urlopen
import urllib
url = 'http://www.amazon.com/'
response = urllib.request.urlopen(url).read()
response
