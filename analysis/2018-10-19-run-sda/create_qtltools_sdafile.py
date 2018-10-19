"Create a file for QTLtools using the output from SDA"


true_genes = {}
def read_pass_genes():
    with open("../../dat/genes-pass-filter.txt") as genes:
        for line in genes:
            line = line.rstrip("\n")
            fields = line.split("\t")
            if fields[1] == "TRUE":
                true_genes[fields[0]] = 1

genes_ind_count = {} #Index by gene id and then individual id
inds = [] #List of individuals

def read_inds():
    with open("../../dat/inds.tsv") as ind_fh:
        for line in ind_fh:
            line = line.rstrip("\n")
            inds.append(line)

read_pass_genes()
read_inds()
with open("../../dat/cell_to_individual_cpm_matrix_standardized_transposedwithnames.tsv", 'rt') as bulk:
    header = bulk.readline()
    components = header.rstrip("\n").split("\t")
    components = components[1:] #Skip first column - "gene"
    for line in bulk:
        line = line.rstrip("\n")
        fields = line.split("\t")
        for i, field in enumerate(fields):
            if i == 0:
                ind1 = field
                genes_ind_count[ind1] = {} #Dict of ind counts for that gene
                continue
            count = float(field)
            genes_ind_count[ind1][components[i - 1]] = count

print("#Chr\tstart\tend\tpid\tgid\tstrand\t" + "\t".join(inds))
start = 1
i = 1
for comp in components:
    line = "MT\t" + str(start) + "\t" + str(start + 1) + "\tcomponent" + str(i) + "\t.\t-"
    for ind1 in inds:
        line = line + "\t" + str(genes_ind_count[ind1][comp])
    print(line)
    i += 1
    start += 100
