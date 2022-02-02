from itertools import product

#seq = "ACGCGGCTCTGAAA"
#frame=3

with open("D:\\coder\\M_projects_Python\\ROSALIND\WorkDir\\rosalind_ba1k.txt") as fp:
    lines = fp.readlines()

seq = lines[0].strip()
frame = int(lines[1].split()[0])

print(frame)


comb = list(product('ACGT',  repeat=frame))
comb = [''.join(i) for i in comb] 
zero=list([0]*len(comb))
dct=dict(zip(comb, zero))
print(comb)

 
for k in dct.keys():
    for i in range(len(seq) - frame +1):
       local_kmer=seq[i:i+frame]
       if local_kmer==k:
           dct[k]+=1
            
            
print(*list(dct.values()))


            