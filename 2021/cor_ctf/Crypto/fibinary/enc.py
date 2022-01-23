import os

fib = [1, 1]
for i in range(2, 11):
	fib.append(fib[i - 1] + fib[i - 2])

print(fib)

def c2f(c):
	n = ord(c)
	b = ''
	for i in range(10, -1, -1):
		if n >= fib[i]:
			n -= fib[i]
			b += '1'
		else:
			b += '0'
	return b


#Decrypt process
#print(os.getcwd())
os.chdir("./cor_ctf/Crypto/fibinary")
enc = open('flag.enc','r').read().split(" ")

flag = ""
for entry in enc:
	val = 0
	ones = [i for i, ltr in enumerate(entry) if ltr == '1']
	print(ones)
	for index in ones:
		val += fib[10-index]
	print(val)
	flag += chr(val)

print(flag)

#Encrypt process 
'''
flag = open('flag.txt', 'r').read()
flag = "flag\{one_two_three\}"
enc = ''
for c in flag:
	enc += c2f(c) + ' '


with open('flag.enc', 'w') as f:
	f.write(enc.strip())
'''

#