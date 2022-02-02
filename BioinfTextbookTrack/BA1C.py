with open('D:\\coder\\M_projects_Python\\ROSALIND\WorkDir\\rosalind_ba1c.txt') as fp:
    lines = fp.readlines()
      
DNA = list(lines[0])
cDNA = [] 

for n in DNA:
    if n == 'A':
        cDNA.append('T')
    elif n == 'T':
        cDNA.append('A')
    elif n == 'C':
        cDNA.append('G')
    else: cDNA.append('C')  

cDNA.reverse()
print(''.join(cDNA))  

 