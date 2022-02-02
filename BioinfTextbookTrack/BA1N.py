
def GenerateArray(k):
    bases = ['A', 'C', 'G', 'T']
    array = bases
    for n in range(k-1):
        array = [i+j for i in array for j in bases]
    return array

def HammingDistance(s1, s2):
    d = sum([1 for i in range(len(s1)) if s1[i]!=s2[i]])
    return d

def Neighbors(pattern, d):
    array = GenerateArray(len(pattern))
    neighbors = []
    for i in array:
        if HammingDistance(pattern, i) <= d:
            neighbors.append(i)
    return neighbors

if __name__ == "__main__":
    # text = 'ACG'
    # d = 1
    with open("D:\\coder\\M_projects_Python\\ROSALIND\WorkDir\\rosalind_ba1n.txt", "r") as fp:
        text = fp.readline().strip()
        d = int(fp.readline().strip())
    for i in Neighbors(text, d):
        print(i)
    