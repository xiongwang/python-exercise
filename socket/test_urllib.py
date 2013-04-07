import urllib2
import urllib
#open a remote address
response = urllib2.urlopen('http://www.google.com')
html = response.read()
print html
print '\n'

urllib.urlretrieve('http://www.google.com', './baidu.html')
