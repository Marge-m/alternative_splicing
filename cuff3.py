def forbed(filewithall, filewithminus, filewithplus):
    f = open(filewithall)
    k = open(filewithminus, 'w')
    n = open(filewithplus, 'w')
    l = []
    for line in f:
        l.append(line.strip().split(' '))
    for item in l:
        if float(item[5]) < 0:
            for i in range(6, len(item)-1, 2):
                k.write(item[0] + ' ' + item[i] + ' ' + item[i+1] + ' ' + item[1] + '\n')
        else:
            for i in range(6, len(item)-1, 2):
                n.write(item[0] + ' ' + item[i] + ' ' + item[i+1] + ' ' + item[1] + '\n')
    k.close()
    n.close()
    f.close()

forbed('filewithborden.txt', 'file2writeminus.txt', 'filetowriteplus.txt')


