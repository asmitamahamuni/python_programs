def count_substring(s, sb):
    count = 0
    for x in range(0, s.__len__()):
        if s[x:x + sb.__len__()] == sb:
            count = count + 1
    return count
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
