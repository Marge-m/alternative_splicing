import pandas as pd


def onlyaltspl(changes): # choose only alternative splicing events from all changes
    iso_changes = pd.read_csv(changes, sep=' ')
    only_alt_spl = pd.DataFrame(columns=['gene_id', 'tracking_id', 'FPKM1', 'FPKM2', 'FPKM_change'])
    loc_count = 0
    print iso_changes
    for iso1 in iso_changes.iterrows():
        for iso2 in iso_changes.iterrows():
            if iso1[1]['gene_id'] == iso2[1]['gene_id'] and iso1[1]['tracking_id'] != iso2[1]['tracking_id']:
                only_alt_spl.loc[loc_count] = iso1[1]
                loc_count += 1
    print only_alt_spl
    return only_alt_spl


def deldupl(changes):  # delete duplicates
    with_duplicates = onlyaltspl(changes)
    without_dup = pd.DataFrame(columns=['gene_id', 'tracking_id', 'FPKM1', 'FPKM2', 'FPKM_change'])
    loc_count = 0
    for iso_with_dup in with_duplicates.iterrows():
        if iso_with_dup[1] not in without_dup:
            without_dup.loc[loc_count] = iso_with_dup[1]
    return with_duplicates


def borden(changes, filewithgenes, f2write):  # write borden
    file_with_borden = open(f2write, 'w')
    without_dup = deldupl(changes)
    genes = pd.read_csv(filewithgenes, sep='\t')
    for iso in without_dup.iterrows():
        isoform_coord = [iso_param for iso_param in iso]
        for gene in genes.iterrows():
            if gene[1]['tracking_id'] == iso['tracking_id'] and gene[1]['region'] == 'exon':
                chrom = gene[1]['chr']
                strand = gene[1]['strand']
                isoform_coord.append(gene[1]['start'])
                isoform_coord.append(gene[1]['end'])
        isoform_coord.insert(0, chrom)
        isoform_coord.insert(len(isoform_coord) - 1, strand)
        file_with_borden.write(' '.join(isoform_coord) + '\n')
    file_with_borden.close()


borden('filewithchanges.txt', 'genes.txt', 'filewithborden.txt')
