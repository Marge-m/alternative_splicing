def onlyaltspl(fname):  # choose only alternative splicing
    f = open(fname)
    l = []
    li = []
    for line in f:
        l.append(line.strip().split(' '))
    for i in range(len(l)):
        for n in range(len(l)):
            if i != n and l[i][0] == l[n][0] and l[i][1] != l[n][1]:
                li.append(l[i])
    return li


def deldupl(fname):  # delete duplicates
    li = onlyaltspl(fname)
    li2 = []
    for item in li:
        if item not in li2:
            li2.append(item)
    return li2


# def abc(fname):
#     f = open(fname)
#     l = []
#     for line in f:
#         l.append(line.strip().split('\t')[0])
#     for item in l:
#         if l.count(item) > 2:
#             print item


def borden(fname, filewithgenes, f2write):  # write borden
    l = deldupl(fname)
    k = open(filewithgenes)
    l2 = []
    for line in k:
        l2.append(line.strip().split('\t'))
    k.close()
    r = open(f2write, 'w')
    for item in l:
        for item2 in l2:
            if item2[11] == item[1] and item2[2] == 'exon':
                k = item2[6]
                chrom = item2[0]
                item.append([item2[3], item2[4]])
        r.write(str(chrom) + ' ')
        for it in item:
            if isinstance(it, str) or isinstance(it, float) or isinstance(it, int):
                r.write(str(it) + ' ')
            else:
                for it2 in map(str, it):
                    r.write(it2 + ' ')
        r.write(str(k) + '\n')
    r.close()


borden('filewithchanges.txt', 'genes-for-splicing4.txt', 'filewithborden.txt')
