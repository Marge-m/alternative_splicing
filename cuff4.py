def final(filewithgenes, filewithisoforms):
    f = open(filewithgenes)
    k = open(filewithisoforms)
    l = []
    l2 = []
    for line in f:
        l.append(line.strip().split('\t'))
    for line in k:
        l2.append(line.strip().split(' '))
    for item in l:
        for i in range(4):
            item.append(None)
        for it in l2:
            if item[3] == it[1]:
                if float(it[5]) < 0:
                    item[5] = it[2]
                    item[6] = it[5]
                else:
                    item[7] = it[2]
                    item[8] = it[5]
    for item in l:
        print '\t'.join(item)

final('SuHw4104.txt', 'filetowrite2.txt')