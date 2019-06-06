import random
import math
from bitarray import bitarray


class BloomFilter:

    def __init__(self, dna_list, p):

        self.dna_list = dna_list
        self.n = len(self.dna_list)
        self.l = len(self.dna_list[0])
        self.p = p
        self.m = math.ceil(-(len(self.dna_list) *
                             math.log(self.p)) / (math.log(2) * math.log(2)))
        self.k = math.ceil(-math.log(self.p) / math.log(2))
        self.bloom_filter = bitarray('0' * self.m)

    def generate_hash(self, dna_sequence):
        """Generates hash function using mmh3 hasing algorithm.Its inbuilt python module."""

        dna = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        list_of_hashes = []

        dna_number = ''
        for i in range(len(dna_sequence)):
            dna_number += str(dna[dna_sequence[i]])
        dna_number = int(dna_number)
        random.seed(dna_number)

        for i in range(self.k):
            a = random.randint(1, dna_number)
            b = random.randint(1, dna_number)
            hash_value = a * i + b
            m_hash = hash_value % self.m
            list_of_hashes.append(m_hash)

        return list_of_hashes

    def insert_to_bloomfilter(self, dna_sequence):
        "inserts dna sequence into bloom filter"

        list_of_hashes = self.generate_hash(dna_sequence)

        for items in list_of_hashes:
            self.bloom_filter[items] = True

    def check(self, dna):
        '''
        Check for existence of an item in filter
        '''
        hash_values = self.generate_hash(dna)
        for items in hash_values:
            if self.bloom_filter[items] == 0:
                return False

        return True
