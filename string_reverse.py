# Reverse the given string

# 1. Reversing a string - Recursive

def reverse(input):
    print(input)
    if len(input) <= 1:
	    return input
	
    return reverse(input[1:]) + input[0]

s = 'reverse'	
print(reverse(s))

# 2. Reversing a string - Iterative

def reverse(input):
    return ''.join([input[i] for i in range(len(input)-1, -1, -1)])
	
s = 'reverse'	
print(reverse(s))
