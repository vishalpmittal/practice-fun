"""
Provide code and solution for Application 4
"""
DESKTOP = True


from json import dumps
from json import loads
import math
import random
import urllib2
from random import shuffle
import numpy as np
from operator import itemgetter

from alg_project4_solution import build_scoring_matrix
from alg_project4_solution import compute_alignment_matrix
from alg_project4_solution import compute_global_alignment
from alg_project4_solution import compute_local_alignment
import matplotlib.pyplot as plt

# if DESKTOP:
#     import matplotlib.pyplot as plt
#     import alg_project4_solution as student
# else:
#     import simpleplot
#     import userXX_XXXXXXX as student

# URLs for data files
# PAM50_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_PAM50.txt"
# HUMAN_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_HumanEyelessProtein.txt"
# FRUITFLY_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_FruitflyEyelessProtein.txt"
# CONSENSUS_PAX_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_ConsensusPAXDomain.txt"
# WORD_LIST_URL = "http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt"

PAM50_URL = "alg_PAM50.txt"
HUMAN_EYELESS_URL = "alg_HumanEyelessProtein.txt"
FRUITFLY_EYELESS_URL = "alg_FruitflyEyelessProtein.txt"
CONSENSUS_PAX_URL = "alg_ConsensusPAXDomain.txt"
WORD_LIST_URL = "assets_scrabble_words3.txt"

###############################################
# provided code
def read_scoring_matrix(filename):
    """
    Read a scoring matrix from the file named filename.  

    Argument:
    filename -- name of file containing a scoring matrix

    Returns:
    A dictionary of dictionaries mapping X and Y characters to scores
    """
    scoring_dict = {}
    # scoring_file = urllib2.urlopen(filename)
    scoring_file = open(filename)
    ykeys = scoring_file.readline()
    ykeychars = ykeys.split()
    for line in scoring_file.readlines():
        vals = line.split()
        xkey = vals.pop(0)
        scoring_dict[xkey] = {}
        for ykey, val in zip(ykeychars, vals):
            scoring_dict[xkey][ykey] = int(val)
    return scoring_dict

def read_protein(filename):
    """
    Read a protein sequence from the file named filename.

    Arguments:
    filename -- name of file containing a protein sequence

    Returns:
    A string representing the protein
    """
    # protein_file = urllib2.urlopen(filename)
    protein_file = open(filename)
    protein_seq = protein_file.read()
    protein_seq = protein_seq.rstrip()
    return protein_seq

def read_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    # load assets
    # word_file = urllib2.urlopen(filename)
    word_file = open(filename)
    
    # read in files as string
    words = word_file.read()
    
    # template lines and solution lines list of line string
    word_list = words.split('\n')
    print "Loaded a dictionary with", len(word_list), "words"
    return word_list

#####################Helper Functions##################
#######################################################
def agreement(xs, ys, scoring):
    align_mat = compute_alignment_matrix(xs, ys, scoring, True)
    score, x, y = compute_global_alignment(xs, ys, scoring, align_mat)
    print "global alignment: "
    print score
    print x
    print y
    similar = [1. for (a, b) in zip(x, ys) if a == b]
    return 100. * len(similar) / len(x)

def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
    distr = {}
    raw = []

    try:
        with open('distr.json') as f:
            pair = loads(f.read())
            return pair['distr'], pair['raw']
    except Exception as e:
        print('cant open file', str(e))

    for _ in range(num_trials):
        temp = list(seq_y)
        shuffle(temp)
        rand_y = ''.join(temp)
        align = compute_alignment_matrix(seq_x, rand_y, scoring_matrix, False)
        score, align_x, align_y = compute_local_alignment(seq_x, rand_y, scoring_matrix, align)
        if score not in distr:
            distr[score] = 0
        distr[score] += 1
        raw.append(score)
    with open('distr.json', 'w') as f:
        f.write(dumps({'distr': distr, 'raw': raw}))
    return distr, raw

def norm(d):
    total = float(sum(d.itervalues()))
    return {k: v / total for k, v in d.iteritems()}

def str_keys(d):
    return {int(k): v for k, v in d.iteritems()}
#######################################################


def question1():
    human = read_protein(HUMAN_EYELESS_URL)
    fly = read_protein(FRUITFLY_EYELESS_URL)

    scoring = read_scoring_matrix(PAM50_URL)
    local_align = compute_alignment_matrix(human, fly, scoring, False)
    score, hum_prot_la, ff_prot_la = compute_local_alignment(human, fly, scoring, local_align)

    print "========question 1=========="
    print "Human eyeless protein length: "+ str(len(human))
    print "Fruitfly eyeless protein length: " + str(len(fly))
    print "Local alignment score: " + str(score)
    print "human protein local alignment string: " + hum_prot_la
    print "fruitfly protein local alignment string: " + ff_prot_la

    ################question 2##############
    print "========question 2=========="
    consensus = read_protein(CONSENSUS_PAX_URL)
    human_nodash = ''.join([x for x in hum_prot_la if x != '-'])
    fly_nodash = ''.join([x for x in ff_prot_la if x != '-'])

    print "consensus: " + consensus
    print ""
    print "Human Agreement...."
    hc_agree = agreement(human_nodash, consensus, scoring)
    print ""
    print "Fruitfly Agreement...."
    fc_agree = agreement(fly_nodash, consensus, scoring)
    print ""
    print('Human vs Consensus agree = %s%%' % hc_agree)
    print('Fly vs Consensus agree = %s%%' % fc_agree)

def question4():
    human = read_protein(HUMAN_EYELESS_URL)
    fly = read_protein(FRUITFLY_EYELESS_URL)
    scoring = read_scoring_matrix(PAM50_URL)
    distr, raw = generate_null_distribution(human, fly, scoring, 1000)

    distr = str_keys(distr)
    distr = norm(distr)
    pairs = list(distr.iteritems())
    pairs = sorted(pairs, key=itemgetter(0))
    index = np.arange(len(pairs))
    barlist = plt.bar(index, map(itemgetter(1), pairs))

    for bar in barlist:
        bar.set_color('c')

    plt.xticks(index + 0.4, map(itemgetter(0), pairs), fontsize=8)
    plt.xlabel('Local Alignment Scores')
    plt.ylabel('Fraction of total trials')
    plt.title('Distribution of scores\nDestop Python 2.7')
    plt.tight_layout()
    plt.savefig("ques4.png")

    s_score = 875
    n = 1000
    mean = sum(raw) / n
    std = np.sqrt(sum((x - mean) ** 2 for x in raw) / n)
    z_score = (s_score - mean) / std

    print('mean = %f' % mean)
    print('std = %f' % std)
    print('z_score = %f' % z_score)

def edit_dist(xs, ys):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    scoring = build_scoring_matrix(alphabet, 2, 1, 0)
    align = compute_alignment_matrix(xs, ys, scoring, True)
    score, x, y = compute_global_alignment(xs, ys, scoring, align)
    return len(xs) + len(ys) - score

def check_spelling(checked_word, dist, word_list):
    return set([word for word in word_list
                if edit_dist(checked_word, word) <= dist])

def question7():
    print "========question7=========="
    dist = edit_dist('hello', 'how')
    print(dist)

    print "========question8=========="
    words = [x.strip() for x in open(WORD_LIST_URL).readlines()]
    humble = check_spelling('humble', 1, words)
    firefly = check_spelling('firefly', 2, words)
    print(len(humble), humble)
    print(len(firefly), firefly)

# question1()
# question4()
question7()

