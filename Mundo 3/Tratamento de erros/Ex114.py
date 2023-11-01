import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[41mO site Pudim não está acessível no momento.\033[m')
else:
    print('Conseguiu acessar o site pudim no momento.')
