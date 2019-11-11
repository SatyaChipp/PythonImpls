# Enter your code here. Read input from STDIN. Print output to STDOUT



def doormat(n, m):
    pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]


    print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
    ##when it reaches half .. print above half again [::-1] for reverse





if __name__ == '__main__':
    doormat(7, 3*7)
