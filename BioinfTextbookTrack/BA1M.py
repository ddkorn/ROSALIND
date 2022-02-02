
def NumberToPattern(index, k):
    bases = ['A', 'C', 'G', 'T']
    pattern = ''
    for i in range(k):
        pattern += bases[index % 4]
        index = index // 4
    return pattern[::-1]

if __name__ == "__main__":
    print(NumberToPattern(6148, 11))