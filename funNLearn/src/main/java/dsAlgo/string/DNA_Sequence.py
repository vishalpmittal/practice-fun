"""
    Tag: string
"""

# ### Prompt One ###
# A base pair is a character in a DNA string.
# DNA is transcribed into by RNA by converting its base pairs according to the following rules:
#     # DNA | RNA
#     # --- | ---
#     #   A | A
#     #   C | C
#     #   T | U
#     #   G | G
# Given a DNA string, convert it to the corresponding RNA string.
# Example:
#     Input:  DNA="CCCTCGATGTTTGTATATTAGCGATCC"
#     Output: RNA="CCCUCGAUGUUUGUAUAUUAGCGAUCC"

# ### Prompt Two ###
# A triplet of base pairs is called a codon.
#     - e.g. DNA="CCCTCGATGTTTGTATATTAGCGATCC" has 9 codons "CCC TCG ATG TTT GTA TAT TAG CGA TCC".
# A gene is the sequence of codons between a START and STOP codon.
#     start_codons = ["AUG"]
#     stop_codons  = ["UAA", "UAG", "UGA"]
# Given a DNA string, retrieve the substring corresponding to a gene.
# Example:
#     Input:          DNA="CCCTCGATGTTTGTATATTAGCGATCC"
#     Output:         GENE="AUGUUUGUAUAUUAG"

# ### Prompt Three ###
# A gene is translated into a protein by converting its codons according to the following rules:
#     # codon | protein
#     # ----- | -------
#     #   AUG | Met
#     #   UUU | Phe
#     #   CGC | Arg
#     #   GUA | Val
#     #   UAU | Tyr
# Given a DNA string, synthesize the encoded protein.
# Example:
#     Input:          DNA="CCCTCGATGTTTGTATATTAGCGATCC"
#     Output:         PROTEIN="Met Phe Val Tyr"
        
dna2rna={
    'A': 'A',
    'C': 'C',
    'T': 'U',
    'G': 'G'  
}
start_codons = {"AUG"}
stop_codons  = {"UAA", "UAG", "UGA"}

gene2protein = {
    'AUG': 'Met', 
    'UUU': 'Phe', 
    'CGC': 'Arg', 
    'GUA': 'Val', 
    'UAU': 'Tyr'
}
    

def dna_to_rna(dna: str) -> str:
    if not dna:
        return None
    rna = ''
    for c in dna:
        rna += dna2rna[c]
    return rna

def get_gene(dna: str) -> str:
    if not dna:
        return None
    
    i = 0
    gene = ''
    while i < len(dna) and not gene:
        rna = dna_to_rna(dna[i: i+3])
        if rna in start_codons:
            gene = rna
        i += 3
        
    if i >= len(dna):
        return None
    
    
    # stop_found = False
    while i < len(dna) : # TO-DO
        rna = dna_to_rna(dna[i: i+3])
        gene += rna        
        
        if rna in stop_codons:
            break

        i += 3
        
    if i >= len(dna):
        return None

    return gene
    

def get_protein(dna: str) -> str:
    if not dna:
        return None
    
    gene = get_gene(dna)
    print(gene)
    i = 0
    protein = ''
    
    while i < len(gene):
        try: 
            if gene[i: i+3] in stop_codons:
                i += 3
                continue
            curr_gene = gene[i: i+3]
            curr_protein = gene2protein[curr_gene]
            protein += curr_protein + ' '
        except KeyError:
             return None
        i += 3
        
    print(protein)
    
    return protein[:-1]
  

assert(dna_to_rna("CCCTCGATGTTTGTATATTAGCGATCC") == "CCCUCGAUGUUUGUAUAUUAGCGAUCC")
assert(get_gene("CCCTCGATGTTTGTATATTAGCGATCC") == "AUGUUUGUAUAUUAG")
assert(get_gene("CCCTCG") == None)
assert(get_gene("CCCTCGATGTTTGTATATCGATCC") == None)
assert(get_protein("CCCTCGATGTTTGTATATTAGCGATCC") == "Met Phe Val Tyr")


print("Tests Passed!")
