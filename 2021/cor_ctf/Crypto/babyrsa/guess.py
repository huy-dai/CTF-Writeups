a = 536712
b = 182482
n = a*b
print("n:",n)

missing = "00"
a1 = "53"
a2 = "12"
a3 = int(a1 + missing + a2)
print("Guess a:",a3)

b1 = "18"
b2 = "82"
b3 = int(b1 + missing + b2)
print("Guess b:",b3)

len = 2
start = 2
end = 2

for i in range(10):
    new_val =  a1 + "0" + str(i) + a2
    new_val = int(new_val)
    print("New val:",new_val)
    res = n - (a3*b3) - (i*b3*pow(10,len))
    print("Leftover",(i*pow(10,len)))
    print(res)
    print(res%new_val)
    if res % new_val == 0:
        print(i,n/new_val)

