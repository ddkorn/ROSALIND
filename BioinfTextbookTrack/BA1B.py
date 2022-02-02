with open('rosalind_ba1b.txt') as fp:
    lines = fp.readlines()

text = lines[0]
k = int(lines[1].strip())
       

def GetkList(Text, K):
    k_lst = []
    for i in range(len(text) - k +1):
        k_lst.append(text[i:i+k])
    return k_lst
   
k_lst = GetkList(text, k)
k_dict = {item: k_lst.count(item) for item in k_lst}


def GetMaxKey(dict):
    for key, val in dict.items():
        if val == max(dict.values()):
            print (key)
            
        
GetMaxKey(k_dict)       


