def forbed(filewithall, filewithminus, filewithplus):
    all_changes = open(filewithall)
    minus = open(filewithminus, 'w')
    plus = open(filewithplus, 'w')
    changes = []
    for line in all_changes:
        changes.append(line.strip().split(' '))
    for change in changes:
        if float(change[5]) < 0:
            for i in range(6, len(change)-1, 2):
                minus.write(change[0] + ' ' + change[i] + ' ' + change[i+1] + ' ' + change[1] + '\n')
        else:
            for i in range(6, len(change)-1, 2):
                plus.write(change[0] + ' ' + change[i] + ' ' + change[i+1] + ' ' + change[1] + '\n')
    minus.close()
    plus.close()
    all_changes.close()

forbed('filewithborden.txt', 'minus_changes.txt', 'plus_changes.txt')


