with open("D:\\coder\\M_projects_Python\\ROSALIND\WorkDir\\rosalind_ba1f.txt") as fp:
    lines = fp.readlines()

str = lines[0]

print(str)
x = 0
CG = []
for i in str:
    CG.append(x) 
    if i == "C":
        x+=1
    elif i == "G":
        x-=1
        
 
    
pos = [i for i,x in enumerate (CG) if x==max(CG)]
print(pos)

