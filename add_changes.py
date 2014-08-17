def changes(fnamewithminus, fnamewithplus, filewithborden, filetowrite):
    f = open(fnamewithminus)
    f2 = open(fnamewithplus)
    k = open(filewithborden)
    r = open(filetowrite, 'w')
    l = []
    l1 = []
    l2 = []
    for line in f:
        l.append(line.strip().split('\t'))
    for line in f2:
        l1.append(line.strip().split('\t'))
    for line in k:
        l2.append(line.strip().split(' '))
    for item in l:
        item.append('minus')
        for i in range(4):
            item.append(None)
        for item2 in l2:
            if item[3] == item2[1]:
                print item2[5]
                if float(item2[5]) < 0:
                    item[9] = item2[2]
                    item[10] = item2[5]
                else:
                    item[11] = item2[2]
                    item[12] = item2[5]
    for item in l:
        r.write('\t'.join(map(str, item)) +'\n')
    for item in l1:
        item.append('plus')
        for i in range(4):
            item.append(None)
        for item2 in l2:
            if item[3] == item2[1]:
                print item2[5]
                if float(item2[5]) < 0:
                    item[9] = item2[2]
                    item[10] = item2[5]
                else:
                    item[11] = item2[2]
                    item[12] = item2[5]
    for item in l1:
        r.write('\t'.join(map(str, item)) + '\n')
    r.close()
    f.close()
    f2.close()

changes('minus_peaks.txt', 'plus_peaks.txt', 'filewithborden.txt', 'total_changes.txt')

