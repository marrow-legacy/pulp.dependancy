# encoding: utf-8

from unittest import TestCase

from pulp.wsgi.graph.util import rotated


class TestRotation(TestCase):
    def test_identical(self):
        seq = ['C', 'D', 'B', 'A']
        self.assertFalse(rotated(seq, seq))
    
    def test_mismatch(self):
        seq1 = ['A', 'B', 'C', 'D']
        seq2 = ['B', 'C', 'D']
        self.assertFalse(rotated(seq1, seq2))
    
    def test_unrelated(self):
        seq1 = ['A', 'B', 'C', 'A']
        seq2 = ['A', 'A', 'C', 'B']
        self.assertFalse(rotated(seq1, seq2))
    
    def test_forward_offset(self):
        seq1 = ['A', 'B', 'C', 'D']
        seq2 = ['C', 'D', 'A', 'B']
        self.assertTrue(rotated(seq1, seq2))
    
    def test_reverse_offset(self):
        seq1 = ['A', 'B', 'C', 'A']
        seq2 = ['A', 'A', 'B', 'C']
        self.assertTrue(rotated(seq1, seq2))
