import binascii

out = ""

with open("export.txt","r") as f:
    f.readline()
    data = f.readline()
    while data != "end":
        val = data.split(",")[2][2:]
        out += val
        data = f.readline()

#print(out)
result = binascii.unhexlify(out).decode('utf-8')
print(result)

result = result.split("\n")


for i in range(0,len(result)):
    if i >= 3 and i < len(result):
        result[i] = result[i][:7] + " C " + result[i][8:]
    result[i] = result[i].replace("S","S ")

for entry in result:
    print(entry)

