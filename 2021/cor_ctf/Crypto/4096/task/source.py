#!/usr/bin/python3

from Crypto.Util.number import getPrime, bytes_to_long
from private import flag
import threading
import os

def prod(lst):
	ret = 1
	for num in lst:
		ret *= num
	return ret

'''
m = bytes_to_long(flag)
primes = [getPrime(32) for _ in range(128)]
print(primes)
n = prod(primes)
e = 65537
print(n)
print(pow(m, e, n))
'''

known = [2724658201,3648309311,2293226687,3303691121]

print(repr(known))

n = 50630448182626893495464810670525602771527685838257974610483435332349728792396826591558947027657819590790590829841808151825744184405725893984330719835572507419517069974612006826542638447886105625739026433810851259760829112944769101557865474935245672310638931107468523492780934936765177674292815155262435831801499197874311121773797041186075024766460977392150443756520782067581277504082923534736776769428755807994035936082391356053079235986552374148782993815118221184577434597115748782910244569004818550079464590913826457003648367784164127206743005342001738754989548942975587267990706541155643222851974488533666334645686774107285018775831028090338485586011974337654011592698463713316522811656340001557779270632991105803230612916547576906583473846558419296181503108603192226769399675726201078322763163049259981181392937623116600712403297821389573627700886912737873588300406211047759637045071918185425658854059386338495534747471846997768166929630988406668430381834420429162324755162023168406793544828390933856260762963763336528787421503582319435368755435181752783296341241853932276334886271511786779019664786845658323166852266264286516275919963650402345264649287569303300048733672208950281055894539145902913252578285197293
i = 0

#Divide by known factors
for fac in known:
	print("Is factor:",n%fac==0)
	n = n // fac

def printit():
  threading.Timer(10.0, printit).start()
  percent = int(i / 203280220 * 100)
  print(percent,"% of the way there")

printit()

print("Starting n:",n)

os.chdir("./cor_ctf/Crypto/4096")

with open("primes.32b", "rb") as f:
	byte = f.read(4)
	while byte != b"":
		if i <= 91476099: #No result under 45% of file read
			byte = f.read(4)
			i += 1
			continue
		val = int.from_bytes(byte, byteorder="little")
		if len(known) == 128: 
			print("Found all the primes")
			break
		if n % val == 0:
			n = n // val
			print("New factor:",val)
			known.append(val)
		byte = f.read(4)
		i +=1

print(repr(known))
'''
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
'''