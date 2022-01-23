from Crypto.Util.number import long_to_bytes
import numpy as np
from pwn import *
from morse import MorseCodeTranslator
import base64
import codecs

def find_invpow(x,n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n < x:
        high *= 2
    low = high//2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1


r = remote("crypto.chal.csaw.io",5001)
translator = MorseCodeTranslator()

while True:
    try:
        print(r.recvuntil("mean?".encode('utf-8')))
    except:
        print(r.recvall())
    chal = r.recvuntil(">>".encode('utf-8'))[2:-4]
    #print(chal)
    decimal = translator.translate_morse(chal.decode('utf-8').replace("/","  "))
    #print(decimal)
    base64_msg = ''.join([chr(int(i)) for i in decimal.split(" ")])
    #print(base64_msg)
    rsa = base64.b64decode(base64_msg).decode('utf-8').split("\n")
    #print(rot13)
    rsa_c = int(rsa[2][4:])
    #print(rsa_c)
    rot13 = long_to_bytes(find_invpow(rsa_c,3)).decode('utf-8')
    #print(rot13)
    ans = codecs.encode(rot13,'rot_13')
    print(ans)
    r.sendline(ans)
    print(r.recvline())

r.close()


