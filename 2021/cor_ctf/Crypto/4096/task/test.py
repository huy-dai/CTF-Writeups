import os

os.chdir("./cor_ctf/Crypto/4096")
print(os.getcwd())

with open("primes.32b", "rb") as f:
    byte = f.read(4)
    i = 0

    while byte != b"" and i <= 20:
        # Do stuff with byte.
        val = int.from_bytes(byte,byteorder="little")
        print(val)
        byte = f.read(4)
        i +=1