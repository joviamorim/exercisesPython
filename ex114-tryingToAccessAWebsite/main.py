import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print("The website is not available in this moment.")
else:
    print("The site is available")
