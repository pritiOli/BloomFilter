from bloomfilter import BloomFilter
import random


def random_dna(length):


"""Generates random dna sequences"""
random_dna_sequence = ''
  dna_string = ['A', 'C', 'G', 'T']

   for j in range(length):
        i = random.randint(0, 3)
        random_dna_sequence += dna_string[i]

    return random_dna_sequence


def evaluation_function(n, l):
    """Evaluation function to test if we get results with expected false positive rate or not
    n = number of DNAs and l is length of each DNA
    """

    number_of_dnas = n
    list_of_dna = []
    for i in range(number_of_dnas):
        dna = random_dna(l)
        list_of_dna.append(dna)
