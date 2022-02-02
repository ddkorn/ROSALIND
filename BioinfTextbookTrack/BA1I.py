import numpy as np
from itertools import product

with open("D:\\coder\\M_projects_Python\\ROSALIND\WorkDir\\rosalind_ba1i.txt") as fp:
    lines = fp.readlines()
    
#seq = lines[0].strip()
#num = lines[1].split()
#frame = int(num[0])
#print(frame)
#mismatch = int(num[1])
#print(mismatch)
    
seq = 'AAAAAAAAAA'
frame = 2 
mismatch = 1 

from BA1E import frame_lst

def hammingDist(seq1, seq2):
    c = [ i for i, j in zip(seq1, seq2) if i != j]
    return len(c)    

def hammingDistBool(Z):
    X,Y = iter(Z)
    distance = mismatch
    scr = hammingDist(X, Y)
    return 1 if scr <= distance else 0

k = frame_lst(seq, frame)[:-frame-1] #получаем список k-mers, удаляем элементы меньшие, чем frame
comb = list(product(k, k))


hd = list(map(hammingDistBool, comb))

hd = np.array(hd)
hd.shape = (len(k), len(k))

hd_sum = np.apply_along_axis(sum, 1, hd)
maximum = max(hd_sum)
dct = dict(zip(k, hd_sum))
MostFreqWords = [] 
print(dct)
for k, v in dct.items():
    if v == maximum:
        MostFreqWords.append(k)
        
print(*MostFreqWords)        
        

#k= frame_lst(seq, frame)[:-frame-1 #получаем список k-mers, удаляем элементы меньшие, чем frame

#comb = list(product(k, k))

#print(x2[:, 0])  # first column of x2