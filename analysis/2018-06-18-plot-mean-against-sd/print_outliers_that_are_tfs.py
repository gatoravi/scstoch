import csv

tfs = {}
def read_tfs():
    with open("/home/aramu/dat/dbd_tf/hs_tf_ass_with_gene_name.tsv") as tfs_fh:
        tfs_dict = csv.DictReader(tfs_fh, delimiter = "\t")
        for tf1 in tfs_dict:
            tfs[tf1['ensembl_gene_id']] = tf1['external_gene_name']

def print_outliers_and_tfs():
    with open("outlier_gene_count.tsv") as outliers:
        outliers_dict = csv.DictReader(outliers, delimiter = " ")
        for outlier1 in outliers_dict:
            if outlier1['gene'] in tfs:
                print(outlier1['gene'] + "\t" + tfs[outlier1['gene']] + "\t" + outlier1['n_ind'])

def main():
    read_tfs()
    print_outliers_and_tfs()

if __name__ == "__main__":
    main()
