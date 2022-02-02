substring = "ATTCTGGA"
string = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC"

with open("D:\\coder\\M_projects_Python\\ROSALIND\WorkDir\\rosalind_ba1h.txt") as fp:
    lines = fp.readlines()

substring = lines[0].strip()
string = lines[1]
num = int(lines[2])

res = []

def PatternMatching(string=string, substring=substring):
    for i, j in enumerate(string[: -len(substring)+1]):
        win = string[i:i+len(substring)]
        #print(i,j)
        c = [m for m, n in zip(win, substring) if m != n] 
        if len(c) <= num: 
        #print( len(c))
          res.append(i) 
    return (res)     

pm = PatternMatching()
pm_str = ' '.join(str(i) for i in pm) 

print(pm_str)
