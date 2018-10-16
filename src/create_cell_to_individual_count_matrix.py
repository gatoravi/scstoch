import gzip

cell_ind = {} #Dictionary to go from cell to individual id
with gzip.open("../dat/scqtl-counts.txt.gz", 'rt') as sc_counts:
    header = sc_counts.readline().rstrip("\n").split("\t")
    for name in header[1:]:
        ind, cell = name.split(".", 1)
        cell = cell.replace(".", "-")
        cell_ind[cell] = ind

with open("../dat/true_genes_cells_cpms.tsv") as true_genes_cells:
    header = true_genes_cells.readline().rstrip("\n").split("\t")
    inds = [] #List of individuals
    genes = [] #List of genes
    ind_gene_count = {}
    for cell in header[1:]:
        ind = cell_ind[cell]
        #If individual not in dictionary
        ind_gene_count[ind] = {}
        inds.append(ind)
    for line in true_genes_cells:
        line = line.rstrip("\n")
        fields = line.split("\t")
        gene = fields[0]
        genes.append(gene)
        for i, field in enumerate(fields[1:]):
            count = float(field)
            ind1 = inds[i] #Get the individual at this index
            if gene not in ind_gene_count[ind1]:
                ind_gene_count[ind1][gene] = 0
            ind_gene_count[ind1][gene] += count

def print_ind_gene_counts():
    print("gene", end = "\t")
    unique_inds = list(set(inds))
    for ind in unique_inds:
        print(ind, end = "\t")
    print("\n", end = "")
    for gene in genes:
        print(gene, end = "\t")
        for ind in unique_inds:
            print(ind_gene_count[ind][gene], end = "\t")
        print("\n", end = "")

print_ind_gene_counts()
