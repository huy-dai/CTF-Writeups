coords = set()
x_coords = []
y_coords = []
with open("./coords.nmea") as f:
    for line in f.readlines():
        line = line.split(",")
        x_coord = float('-'+line[2])
        y_coord = float(line[4])
        z_coord = float(line[9])
        x_coords.append(x_coord)
        y_coords.append(y_coord)
        coords.add((x_coord,y_coord,z_coord))
        #print(str(x_coord)+"," +str(y_coord)+",")
for coord in coords:
    print(coord,",")
print(max(x_coords),min(x_coords))
print(max(y_coords),min(y_coords))

'''
bin = ""
for x in range(54,30,-1):
    for y in range(-39,-19):
        if (float(x),float(y)) in coords:
            bin += "."
        else:
            bin += "-"
print(bin)
'''
