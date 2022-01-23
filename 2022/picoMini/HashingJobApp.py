from pwn import *
import hashlib 


conn = remote("saturn.picoctf.net",51108)
res = ""

while "picoCTF" not in res:
    res = conn.recvline().decode('utf-8')[:-2]
    print(res)
    try:
        quote = res[res.index("\'")+1:-1]
    except:
        print(res)
    print("Quote:",quote)

    md5sum = hashlib.md5(quote.encode()).hexdigest()
    print(conn.recvline()) #Ignore line
    conn.sendline(md5sum.encode()) #Send answer
    res = conn.recvline().decode()
    res = conn.recvline().decode()
    print(res)
        

conn.close()