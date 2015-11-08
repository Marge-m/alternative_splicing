"""
This script filter isoforms with initial/final FPKM >= 5.0 and then filter isoforms 
which ratio 'isoform FPKM to gene FPKM' has changed by more than 0.5
"""


import pandas as pd


def filter_isoforms(fpkmlist):
    ai = pd.read_csv(fpkmlist, sep='\t') # ai = all isoforms
    return ai[(ai.q1_FPKM >= 5) | (ai.q2_FPKM >= 5)].loc[:, ['gene_id', 'tracking_id', 'q1_FPKM', 'q2_FPKM']]
    # return isoforms with initial or final FPKM >= 5


def changes(fpkmlist, f2write, genes_fpkm):  # print out isoforms with changes, which exceed 0.5 (change in isoform FPKM to gene FPKM ratio)
    filtered = filter_isoforms(fpkmlist)
    genes = pd.read_csv(genes_fpkm, sep='\t') # fpkm for genes
    iso_exc_stdev = pd.DataFrame(columns=['gene_id', 'tracking_id', 'FPKM1', 'FPKM2', 'FPKM_change'])
    loc_count = 0
    for isoform in filtered.iterrows():
        for gene in genes.iterrows():
            if gene[1]['tracking_id'] == isoform[1]['gene_id']:
                gene_fpkm_init = gene[1]['q1_FPKM']
                gene_fpkm_final = gene[1]['q2_FPKM']
                break
        if gene_fpkm_init != 0 and gene_fpkm_final != 0: #count standard deviation of changes in isoform's fpkm percentage in their genes fpkm
            if abs((isoform[1]['q2_FPKM']/gene_fpkm_final - isoform[1]['q1_FPKM']/gene_fpkm_init)) > 0.5:
                iso_exc_stdev.loc[loc_count] = [isoform[1]['gene_id'], isoform[1]['tracking_id'], isoform[1]['q1_FPKM']/gene_fpkm_init, isoform[1]['q2_FPKM']/gene_fpkm_final, isoform[1]['q2_FPKM']/gene_fpkm_final - isoform[1]['q1_FPKM']/gene_fpkm_init]
                loc_count += 1
        if gene_fpkm_init == 0:
            if isoform[1]['q2_FPKM']/gene_fpkm_final > 0.5:
                iso_exc_stdev.loc[loc_count] = [isoform[1]['gene_id'], isoform[1]['tracking_id'], 0, isoform[1]['q2_FPKM']/gene_fpkm_final, isoform[1]['q2_FPKM']/gene_fpkm_final]
                loc_count += 1
        if gene_fpkm_final == 0:
            if isoform[1]['q1_FPKM']/gene_fpkm_init > 0.5:
                iso_exc_stdev.loc[loc_count] = [isoform[1]['gene_id'], isoform[1]['tracking_id'], isoform[1]['q1_FPKM']/gene_fpkm_init, 0, - isoform[1]['q1_FPKM']/gene_fpkm_init]
                loc_count += 1
    iso_exc_stdev.to_csv(f2write, sep='\t')


changes('isoforms.fpkm_tracking', 'filewithchanges.txt', 'genes.fpkm_tracking')


