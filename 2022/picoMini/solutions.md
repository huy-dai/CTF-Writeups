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

## PW Crack 3

Category: General Skills
Points: 75

The python file provides 8 options for you to enter, one of which is the correct answer. It's a plug and chug problem.

Flag: picoCTF{m45h_fl1ng1ng_024c521a}


## PW Crack 4

Category: General Skills
Points: 85

Now with 100 possibilities, we simply add code in the Python file to test all options and print out the correct option.

~~~py
# The strings below are 100 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["b5e5", "71ff", "acaf", "390c", "1a9b", "e7e2", "a35c", "fafd", "b759", "5eba", "6506", "d5ce", "2df5", "476b", "ca78", "8797", "821c", "28e7", "2bcb", "7906", "6c2a", "734e", "ad9a", "7acd", "6c65", "8d90", "6c81", "b3a8", "bfac", "d96e", "8d45", "b365", "2bf7", "bec9", "25c8", "c716", "1854", "75d0", "9084", "a891", "e863", "d754", "5486", "d652", "a529", "af06", "2b97", "3e5c", "6c7d", "9d26", "5db7", "69cc", "e304", "94cf", "e7c9", "67c7", "df95", "8858", "9319", "b91e", "1ff8", "ed2e", "9628", "70ba", "2ea8", "a5d8", "d59b", "a0c6", "2f25", "f7ba", "db04", "c53f", "e2f7", "bf10", "1392", "ff42", "31d4", "edab", "5bea", "dd25", "32e6", "980e", "8286", "23e8", "4379", "88cc", "de9a", "92dd", "4922", "7c82", "c054", "6587", "e655", "5c39", "ab8c", "29b3", "443c", "31f9", "fbff", "a08f"]

for pos in pos_pw_list:
    hashed = hash_pw(pos)
    if hashed == correct_pw_hash:
        decryption = str_xor(flag_enc.decode(), pos)
        print(decryption)
~~~

Flag: picoCTF{fl45h_5pr1ng1ng_e7668ddf}

## PW Crack 5

Category: General Skills
Points: 85

Similar cracking premise as PW Crack 5, except now we are given a dictionary of all 4 letter long words.

Modified script file: 
~~~py
def level_5_pw_check(hash):
    #user_pw = input("Please enter correct password for flag: ")
    user_pw = hash
    user_pw_hash = hash_pw(hash)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    #print("That password is incorrect")

#level_5_pw_check()

with open("dictionary.txt","r") as f:
    for line in f.readlines():
        level_5_pw_check(line[:-1])
~~~

Flag: picoCTF{h45h_sl1ng1ng_40f26f81}