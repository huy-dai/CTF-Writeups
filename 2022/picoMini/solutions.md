# PicoMini 2022

This is a month-long event ran in January 2022 aimed at beginners wanting to get started in CTF. I wanted to take a crack at the problems to see their difficulty and consider how useful this mini-competition may be for TechSec club members.

## runme.py

Category: General Skills
Points: 5

Run the Python script

Flag: picoCTF{run_s4n1ty_run}

## ncme

Category: General Skills
Points: 10

Run the provided netcat command.

Flag: picoCTF{s4n1ty_c4t}

## convertme.py

Category: General Skills
Points: 15

The Python program ask for a decimal to binary conversion. Interestingly, the file uses an xor key encryption to hide the true value of the text until the user correctly answers the question. This process can be easily reversed, though it is not necessary for this question.

Flag: picoCTF{4ll_y0ur_b4535_722f6b39}

## Codebook

Category: General Skills
Points: 20

Same as last problem but this problem has an added text file.

Flag: picoCTF{c0d3b00k_455157_687087ee}

## fixme1.py

Category: General Skills
Points: 25

The identation was off in the python script.

Flag: picoCTF{1nd3nt1ty_cr1515_79fb5597}

## fixme2.py

Category: General Skills
Points: 25

The equality check needed an extra equal sign = .

Flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_f6a5aefc}

## PW Crack 1

Category: General Skills
Points: 25

The file was checking for user input equals "60ab"

Flag: picoCTF{545h_r1ng1ng_c26330ca}

## Glitch Cat

Category: General Skills
Points: 30

We just need to evaluate the Python expression

~~~py
res = 'picoCTF{gl17ch_m3_n07_' + chr(0x38) + chr(0x31) + chr(0x31) + chr(0x66) + chr(0x66) + chr(0x66) + chr(0x65) + chr(0x65) + '}'
print(res)
~~~

Flag: picoCTF{gl17ch_m3_n07_811fffee}

## PW Crack 2

Category: General Skills
Points: 30

The expected password string as "39ce"

Flag: picoCTF{tr45h_51ng1ng_502ec42e}

## HasingJobApp

Category: General Skills
Points: 40

This problem wanted for us to get the md5 hash of various strings. I decided to over-engineer this problem and write a solve script to automate the tasks.

~~~py
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
~~~

Flag: picoCTF{4ppl1c4710n_r3c31v3d_bf2ceb02}

## Serpentine

Category: General Skills
Points: 50

The challenge wants us to change the Python file to call the `print_key()` function.

Flag: picoCTF{7h3_r04d_l355_7r4v3l3d_569ab7a6}

