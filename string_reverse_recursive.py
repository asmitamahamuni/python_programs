# Reversing a string - Recursive

def reverse(input):
    print(input)
    if len(input) <= 1:
	    return input
	
    return reverse(input[1:]) + input[0]

s = 'reverse'	
print(reverse(s))
