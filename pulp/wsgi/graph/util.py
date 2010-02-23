# encoding: utf-8

"""Utility functions to facilitate dependancy graph generation."""


__all__ = ['rotated']


def rotated(seq1, seq2):
    "Return true if the first sequence is a rotation of the second sequence."
    
    len1 = len(seq1)
    len2 = len(seq2)
    
    if len1 != len2:
        return False
    
    if seq1 == seq2:
        return False
    
    head_item = seq2[0]
    
    def start_indexes():
        for index1 in range(len1):
            if seq1[index1] == head_item:
                yield index1
    
    double_seq1 = seq1 + seq1
    for index1 in start_indexes():
        if double_seq1[index1:index1+len1] == seq2:
            return True
    
    return False
