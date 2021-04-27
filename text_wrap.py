import textwrap

def wrap(string, max_width):
    newtext = textwrap.wrap(string, max_width)
    a = '\n'.join(newtext)
    return a

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
    
#Input :

#ABCDEFGHIJKLIMNOQRSTUVWXYZ
#4
