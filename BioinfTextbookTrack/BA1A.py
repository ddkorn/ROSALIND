with open("D:\\coder\\M_projects_Python\\ROSALIND\WorkDir\\rosalind_ba1a.txt") as fp:
    lines = fp.readlines()

text = lines[0]
pattern = lines[1].strip()

   
def PatternCount(Text, Pattern):
   count = 0
   for i in range(len(text) - len(pattern) + 1):
       if text[i:i+len(pattern)] == pattern:
           count+=1
   return count        
        
                     
print(PatternCount(text, pattern))     

                                                
