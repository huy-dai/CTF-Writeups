mapping = [
    (1, "1koZPp9re_VJzEU_DNnsSv5xj8QUOWtdL3fjd_lLJCLUbcMc4CQHyAlFH"),
    (1, "pcTNrWo"),
    (11, "SstG2T3VOeBzXuf7vbe5ZYHfmgZ_EVviRH6LbkgVfCUKnD"),
    (11,"LjULhLkhPILFXBR3FtcsOWxvKn1prtZfd0g"),
    (11,"xFpT"),
    (11,"ie3"),
    (11,"t"),
    (16,"W1Gm0ANaYQTl0u9TVlrNxttweVQ8B6v"),
    (16,"6C0DIbIdPm_"),
    (16,"uQY_I7gx5"),
    (16,"_J"),
    (17,"is"),
    (20,"bauRW6"),
    (22,"D8_"),
    (22,"4"),
    (23,"d"),
    (25,"4"),
    (27,"y"),
    (3,"t1zUg"),
    (30,"HoUBRagyMy6BY78x"),
    (30,"_"),
    (31,"j"),
    (33,"HqrgItMkQddlD_"),
    (33,"h7x04fO4Crt"),
    (33,"s"),
    (35,"bQC2r2zh0l"),
    (35,"guw4QHt"),
    (35,"_SEA"),
    (36,"4sip"),
    (38,"k"),
    (39,"_"),
    (4,"f{jtE"),
    (41,"rr"),
    (41,"A"),
    (48,"1U90zDT0mZ"),
    (50,"0Sp07t0p"),
    (50,"keO"),
    (50,"3t"),
    (50,"3"),
    (55,"h}q"),
    (6,"o1"),
    (6,"b"),
    (8,"U"),
]


out = ["*"]*60
for [start,seq] in mapping:
    for i in range(0,len(seq)):
        out[start-1+i] = seq[i]

print("".join(out)) #missing b at the start


