# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 12:23:53 2020

@author: Dasha
"""
with open("D:\\coder\\M_projects_Python\\ROSALIND\WorkDir\\rosalind_ba1g.txt") as fp:
    lines = fp.readlines()

seq1 = lines[0]
seq2 = lines[1]

c = [ i for i, j in zip(seq1, seq2) if i != j]
print(len(c))