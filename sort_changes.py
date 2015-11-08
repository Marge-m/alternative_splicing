import pandas as pd


def forbed(filewithall, filewithminus, filewithplus):
    all_changes = open(filewithall)
    changes = []
    minus_changes = pd.DataFrame(columns=['chr', 'start', 'end', 'gene_id'])
    plus_changes = pd.DataFrame(columns=['chr', 'start', 'end', 'gene_id'])
    minus_start = 0
    plus_start = 0
    for line in all_changes:
        changes.append(line.strip().split(' '))
    all_changes.close()
    for change in changes:
        if float(change[5]) < 0:
            for i in range(6, len(change)-1, 2):
                minus_changes.loc[minus_start] = [change[0], change[i], change[i+1], change[1]]
                minus_start += 1
        else:
            for i in range(6, len(change)-1, 2):
                plus_changes.loc[plus_start] = [change[0], change[i], change[i+1], change[1]]
                plus_start += 1
    minus_changes.to_csv(filewithminus, sep=' ')
    plus_changes.to_csv(filewithplus, sep=' ')

forbed('filewithborden.txt', 'minus_changes.txt', 'plus_changes.txt')
