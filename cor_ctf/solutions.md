# My solutions for the Cor CTF 2021

Website link to competition homepage: <https://2021.cor.team/>. The points value are based on the final values at the end of the competition (the problems value depreciates with more solves)

## Problems that I could solve

There were 3 problems out of 35 that I was able to solve during the entire competition (a depressing number if you ask me), all of them being RSA. I'll also be looking over people's writeups of competition problems to see what I could learn from them. 
## Fibinary

Category: Crypto
Points: 205

We were given a file which encrypts the flag character-by-character using the following function:

~~~py
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
~~~

We can see that c2f gets the ASCII value of the character, and then proceeds to convert it into fibonacci-binary (a term I just made up) using the 1st through 10th fibonacci numbers. To decrypt, we can simply read in the fib-binary output and add up the value of each digits to get back the original ASCII value.

~~~py
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
~~~

Thus, this text:

~~~text
10000100100 10010000010 10010001010 10000100100 10010010010 10001000000 10100000000 10000100010 00101010000 10010010000 00101001010 10000101000 10000010010 00101010000 10010000000 10000101000 10000010010 10001000000 00101000100 10000100010 10010000100 00010101010 00101000100 00101000100 00101001010 10000101000 10100000100 00000100100
~~~

yields `corctf{b4s3d_4nd_f1bp!113d}`

Flag: corctf{b4s3d_4nd_f1bp!113d}

## 4096

Category: Crypto
Points: 360

The challenge had encrypted the flag in RSA using 128 randomly generated 32-bit primes multiplied together to produce `n`. Even though 4096-bit RSA key sounds secure in theory, since there is only a limited number of 32-bit primes (203280220 unique primes, in fact), we can brute-force the factors by iterating over all 32-bit primes.

My initial naive approach involved repatedly calling `getPrimes()` function from Crypto.Util.number as it was used in the encryption process to randomly generate 32-bit primes and check if they divides n. However, I quickly found this approach to be ineffective as it retrieved a new factor every ~10 minutes. 

Guessing random primes:

~~~py
def test_prime():
	while True:
		primes = [getPrime(32) for _ in range(256)]
		for p in primes:
			if n % p == 0:
				print("New factor:",p)
~~~

I tried even to use the `Threading` module to take advantage of multiple cores, though this too was too slow of a method.
~~~py
exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name + '\n')
      test_prime()


def test_prime():
	while True:
		primes = [getPrime(32) for _ in range(256)]
		for p in primes:
			if n % p == 0:
				print("New factor:",p)

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")
~~~

After a bit of searching I found that there was a pre-computed databse of all 32-bit primes [here](http://www.umopit.ru/CompLab/primes32eng.htm). The database is given as a binary file where each 4 bytes represent a prime number stored in little endian format. With that, I was able to create a new script that iterates over all the 32-bit primes and retrieve the 128 factors of `n`. Note: To use the [source.py](Crypto/4096/task/source.py) script you need to download the database again since Github will yell at me if I push a ~300 MB binary file.

Since I already had a script from another CTF (C2C CTF) that could solve multi-primes RSA (e.g., when `n` has more than 2 factors), I was able to bring it over and use it to decrypt the flag (found at [rsa_solver.py](Crypto/4096/task/rsa_solver.py)).

Flag: corctf{to0_m4ny_pr1m3s55_63aeea37a6b3b22f}

## Dividing Secrets

Category: Crypto
Points: 434

Contrary to normal RSA where you encrypt the message by doing `m^e mod n`, here they decided to do `e^m mod n`. There's also no correlation between `e` and `n` except that `e < n` and that `n` is a prime number. The web service they give us allow us to provide a number which will be used to output `e^(m//input) mod n`.

I'm not sure if there was a more mathematically-informed way of solving this problem, but the way that I did it was using binary search to get the value of the `m` or the flag. We know that if `input > m` then `m//input = 0` and the output will be 1. Otherwise the result will be `e` (if we are close) or some other value. Also, since the flag remains static across each call to the server, we can perform this operation many times until we arrive at value of `m`.

My exploit script looks like this:

~~~py

#Chose random p for hi
i = 0
hi = 12123011818658592223829585444463227444387063694309686111263422100048399811440660891168952304033795717311157503302903808212679523140543340266855141269464379
low = 1

while hi - low != 1:
    print("Trial:",i)
    print("High:",hi)
    print("Low:",low)
    avg = (hi + low) // 2
    r.sendline(str(avg).encode('utf-8'))
    res = r.recvline().decode('utf-8')
    if i == 0:
        res = int(res)
    elif "no more tries" in res:
        #Close current r and make new connection
        r.close()
        r = remote('crypto.be.ax',6000)
        res = r.recvuntil(b">").decode('utf-8')
        i = 0
        continue
    else:
        res = int(res[res.index("> ")+2:])
    print("Result:",res)
    print(type(res))
    if res == 1: #avg >= flag
        hi = avg
    else: #avg < flag
        low = avg
    i+=1

r.close()
~~~

Once I arrived at a hi and low bound that are within 2 of each other I could simply print out their long_to_bytes equivalence and get the flag:
Full script is at [exp.py](Crypto/Dividing_Secrets/exp.py)

Flag: corctf{qu4drat1c_r3s1due_0r_n0t_1s_7h3_qu3st1on8852042051e57492}


## Problems that I couldn't solve 

There were a few problems that I attempted but was not able to successfully solve. After reading people's writeups, I'll try to detail their solution below (including how I had tried to go about it).

