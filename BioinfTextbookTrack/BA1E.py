from collections import Counter 
import time


start = time.monotonic()


with open("D:\\coder\\M_projects_Python\\ROSALIND\WorkDir\\rosalind_ba1e.txt") as fp:
    lines = fp.readlines()

seq = lines[0]
numbers = lines[1].split()

step = int(numbers[0])
frame = int(numbers[1])
value = int(numbers[2])

#Вывод всех последовательностей с заданной рамком считывания
def frame_lst(seq, frame):
    return [seq[i:i+frame] for i in range(len(seq))]
    
#Все рамки считывания
seq = frame_lst(seq, frame)

#Все k-меры в рамках считывания
pattern = list(map(lambda x: frame_lst(x, step) , seq))
dct_lst = [dict(Counter(i)) for i in pattern]

#Получить ключи
def get_key(d, value,):
    for k, v in d.items():
        if v == value:
            return k
      
        
my_patterns = [get_key(i, value) for i in dct_lst]
my_patterns = filter(None, my_patterns) 
my_patterns = list(set(my_patterns))
my_patterns = ' '.join(my_patterns)
print(my_patterns)

result = time.monotonic() - start
print("Program time: {:>.3f}".format(result) + " seconds.")

