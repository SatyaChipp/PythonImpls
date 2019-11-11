def print_rangoli(size):
    # your code goes here
    import string
    alpha = list(string.ascii_lowercase)
    alpha2 = [chr(i) for i in range(ord('a'),ord('z')+1)] #another way to get alphabets
    output = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        
        output.append((s[::-1]+s[1:]).center(4*size-3, "-"))
        
    print('\n'.join(output[:0:-1] + output))
        

if __name__ == '__main__':
    print_rangoli(5)