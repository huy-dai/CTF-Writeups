offset = 0xCafe

indices = [0,6,5,1,9,10,4,3,8,7,2,11]
vals = [52037,52081,52063,52077,52077,52080,52046,52066,52085,52081,52077,52066]

dic = dict()
for i in range(12):
    dic[indices[i]] = vals[i]

password = ""
for i in range(12):
    password += chr(dic[i] - offset)

print(password)

