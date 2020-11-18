#-*-coding:utf-8-*-
##integrate cdr and ncbi training data chemical text into
def read_ctd_chemical_text_and_output(input_file1, input_file2, out_file):
    cdr_texts = []
    with open(input_file2, 'r') as fr2:
        for line in fr2:
            if(line.strip().lower() not in cdr_texts):
                cdr_texts.append(line.strip().lower())
    fw = open(out_file,"w")
    for cdr_text in cdr_texts:
        fw.write(cdr_text+"\n")

    fr = open(input_file1, "r")
    line = fr.readline().strip().lower()
    while line:
        if line not in cdr_texts:
            fw.write(line+"\n")
        line = fr.readline().strip().lower()
    fr.close()

    fw.close()

def parser_gene_stv(in_file, out_file):
    gene_texts = []
    fr = open(in_file, "r")
    line = fr.readline().strip().lower()
    while line:
        if line.startswith("#"):
            line = fr.readline().strip().lower()
            continue
        linesplits = line.split("\t")

        name = linesplits[1].strip()

        if name not in gene_texts and name:
            gene_texts.append(name)
        if len(linesplits) > 4:
            syns = linesplits[4].strip()
            if syns:
                synsplit = syns.split("|")
                if len(line) > 0:
                    for syns in synsplit:
                        if syns not in gene_texts and syns:
                            gene_texts.append(syns)
        line = fr.readline().strip().lower()
    fw = open(out_file, "w")
    for gene_text in gene_texts:
        fw.write(gene_text + "\n")
    fw.close()




def out_chemical_text(out_file, texts):

    with open(out_file, 'w') as fp:
        for str in texts:
            fp.write(str+"\n")

def parser_gene_onto(gene_onto,out_gene_texts):
    gene_texts = set()


    with open(gene_onto, "r")as fr:
        for line in fr.readlines():
            if line:
                if line.find("name:") != -1:
                    name = line[5:]
                    name = name.strip().lower()
                    gene_texts.add(name)
                if line.find("synonym:") != -1:
                    l_start = line.index('\"')
                    r_end = line.rindex('\"')
                    syn = line[l_start + 1: r_end]
                    syn = syn.strip().lower()
                    gene_texts.add(syn)

    fw = open(out_gene_texts, "w")
    for gene_text in gene_texts:
        fw.write(gene_text + "\n")
    fw.close()


if __name__ == '__main__':
    gene_onto =   
    out_gene_texts = 
    parser_gene_onto(gene_onto,out_gene_texts)

