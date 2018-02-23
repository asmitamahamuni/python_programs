# Print Hamming distance for give two strings : 

def hamming(s1,s2): 
    if len(s1) != len(s2): 
        raise ValueError("Not defined - unequal lenght sequences") 
    return sum(c1 != c2 for c1,c2 in zip(s1,s2))

if __name__ == '__main__': 
    print(hamming("karolin", "kathrin")) # 3 
    print(hamming("karolin", "kerstin")) # 3 
    print(hamming("1011101", "1001001")) # 2
    print(hamming("2173896", "2233796")) # 3
