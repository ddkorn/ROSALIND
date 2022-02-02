
with open('D:\\coder\\M_projects_Python\\ROSALIND\WorkDir\\test.txt') as fp:
    lines = fp.readlines()

pattern = lines[0].strip()
seq = lines[1].strip()
#print(type(pattern))
   
def PatternPosition(Text, Pattern):
    position = []
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i+len(Pattern)] == Pattern:
            position.append(i)
    return position  


print(PatternPosition(seq, pattern))
