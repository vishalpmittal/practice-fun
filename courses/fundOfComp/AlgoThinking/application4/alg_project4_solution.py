"""
Course : Algorithmic Thinking (Part 2)
Instructor: Luay Nakhleh, Scott Rixner, Joe Warren
Project 4 - Computing alignments of sequences
Date: 11/07/2015
Author: Vishal Mittal
"""
def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """
    builds a scoring matrix as a dictionary of dictionaries
    Input: set of characters alphabet and three scores 
            diag_score, off_diag_score, and dash_score
    Output: returns a dictionary of dictionaries whose entries are indexed 
            by pairs of characters in alphabet plus '-'
    """
    all_alph = alphabet.copy()
    all_alph.add("-")
    score_dict = {}
    for char in all_alph:
        score_dict[char] = {}
    for outer in all_alph:
        for inner in all_alph:
            if outer == "-" or inner == "-":
                score_dict[outer][inner] = dash_score
            elif outer == inner:
                score_dict[outer][inner] = diag_score
            else:
                score_dict[outer][inner] = off_diag_score
    return score_dict

def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """
    Input: two sequences seq_x and seq_y whose elements share a common 
            alphabet with the scoring matrix scoring_matrix
    Output: computes and returns the alignment matrix for seq_x and seq_y 
    """
    len_row = len(seq_x) + 1
    len_col = len(seq_y) + 1

    align_matrix = [ [None for dummy_col in range(len_col)] for dummy_row in range(len_row)]
    align_matrix[0][0] = 0

    for row_indx in range(1, len_row):
        align_matrix[row_indx][0] = align_matrix[row_indx-1][0] + scoring_matrix[seq_x[row_indx-1]]["-"]
        if not global_flag and align_matrix[row_indx][0]<0:
            align_matrix[row_indx][0]=0

    for col_indx in range(1, len_col):
        align_matrix[0][col_indx] = align_matrix[0][col_indx-1] + scoring_matrix[seq_y[col_indx-1]]["-"]
        if not global_flag and align_matrix[0][col_indx]<0:
            align_matrix[0][col_indx]=0

    for row_indx in range(1, len_row):
        for col_indx in range(1, len_col):
            val_one = align_matrix[row_indx-1][col_indx-1] + scoring_matrix[seq_x[row_indx-1]][seq_y[col_indx-1]]
            val_two = align_matrix[row_indx-1][col_indx] + scoring_matrix[seq_x[row_indx-1]]["-"]
            val_three = align_matrix[row_indx][col_indx-1] + scoring_matrix["-"][seq_y[col_indx-1]]
            value = max(val_one, val_two, val_three)
            if not global_flag and value < 0:
                align_matrix[row_indx][col_indx] = 0
            else:
                align_matrix[row_indx][col_indx] = value
    return align_matrix

def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    computes a global alignment of seq_x and seq_y using the global 
    alignment matrix alignment_matrix
    Input: two sequences seq_x and seq_y whose elements share a common 
            alphabet with the scoring matrix scoring_matrix
    Output: returns a tuple of the form (score, align_x, align_y)
    """
    row_indx = len(seq_x)
    col_indx = len(seq_y)
    align_x = ""
    align_y = ""

    while row_indx != 0 and col_indx != 0:
        if alignment_matrix[row_indx][col_indx] == alignment_matrix[row_indx-1][col_indx-1] + scoring_matrix[seq_x[row_indx-1]][seq_y[col_indx-1]]:
            align_x = seq_x[row_indx-1] + align_x
            align_y = seq_y[col_indx-1] +align_y
            row_indx -= 1
            col_indx -= 1

        elif alignment_matrix[row_indx][col_indx] == alignment_matrix[row_indx-1][col_indx] + scoring_matrix[seq_x[row_indx-1]]["-"]:
            align_x = seq_x[row_indx-1] + align_x
            align_y = "-" + align_y
            row_indx -= 1

        else:
            align_x = "-" + align_x
            align_y = seq_y[col_indx-1] + align_y
            col_indx -= 1

    while row_indx != 0:
        align_x = seq_x[row_indx-1] + align_x
        align_y = "-" + align_y
        row_indx -= 1

    while col_indx != 0:
        align_x = "-" + align_x
        align_y = seq_y[col_indx-1] + align_y
        col_indx -= 1

    return (alignment_matrix[len(seq_x)][len(seq_y)], align_x, align_y)

def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    computes a local alignment of seq_x and seq_y using the local 
    alignment matrix alignment_matrix.
    Input: two sequences seq_x and seq_y whose elements share a common 
            alphabet with the scoring matrix scoring_matrix
    Output: returns a tuple of the form (score, align_x, align_y) 
    """
    score = -1
    highest_x = 0
    highest_y = 0
    for row_indx in range (0,len(seq_x)+1):
        for col_indx in range (0, len(seq_y)+1):
            if alignment_matrix[row_indx][col_indx] >= score:
                score = alignment_matrix[row_indx][col_indx]
                highest_x = row_indx
                highest_y = col_indx

    row_indx = highest_x
    col_indx = highest_y

    align_x = ""
    align_y = ""
    while alignment_matrix[row_indx][col_indx] != 0:
        if alignment_matrix[row_indx][col_indx] == alignment_matrix[row_indx-1][col_indx-1] + scoring_matrix[seq_x[row_indx-1]][seq_y[col_indx-1]]:
            align_x = seq_x[row_indx-1] + align_x
            align_y = seq_y[col_indx-1] +align_y
            row_indx -= 1
            col_indx -= 1

        elif alignment_matrix[row_indx][col_indx] == alignment_matrix[row_indx-1][col_indx] + scoring_matrix[seq_x[row_indx-1]]["-"]:
            align_x = seq_x[row_indx-1] + align_x
            align_y = "-" + align_y
            row_indx -= 1

        else:
            align_x = "-" + align_x
            align_y = seq_y[col_indx-1] + align_y
            col_indx -= 1

    return (score, align_x, align_y)

#  expected {'A': {'A': 6, 'C': 2, '-': -4, 'T': 2, 'G': 2}, 'C': {'A': 2, 'C': 6, '-': -4, 'T': 2, 'G': 2}, '-': {'A': -4, 'C': -4, '-': -4, 'T': -4, 'G': -4}, 'T': {'A': 2, 'C': 2, '-': -4, 'T': 6, 'G': 2}, 'G': {'A': 2, 'C': 2, '-': -4, 'T': 2, 'G': 6}} 
# print build_scoring_matrix(set(['A', 'C', 'T', 'G']), 6, 2, -4)

# alphabets = set(['A', 'C', 'T', 'G'])
# seq_x = "AC"
# seq_y = "TCAAT"
# scoring_matrix = build_scoring_matrix(alphabets, 10, 4, -6)
# print scoring_matrix
# alignment_matrix = compute_alignment_matrix(seq_x, seq_y, scoring_matrix, False)
# print alignment_matrix

# global_align_result = compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
# print global_align_result

# local_align_result = compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
# print local_align_result
