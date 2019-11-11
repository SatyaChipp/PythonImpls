# Complete the getScore function below.
get the count of the number of distince palindromes for a given string
-- below not optimized -- O(n^2)
bring Big O down or change lang to Java or C++

from itertools import combinations
def getScore(s):
    def get_combination(string):
        string_array = []
        for y in range(len(string)-1,1,-1):
            for x in combinations(string,y):
                if ''.join(x)==''.join(x)[::-1]:
                    string_array.append(''.join(x))
                    break
        return string_array
    palindrome_len = []
    for i in range(0, len(s)):
        str1_array = []
        str2_array = []
        string1 = s[:i]
        string2 = s[i:]
        str1_array = get_combination(string1)
        str2_array = get_combination(string2)
        if str1_array and str2_array:
            palindrome_len.append(len(str1_array[0]) * len(str2_array[0]))
    return max(palindrome_len)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    res = getScore(s)

    fptr.write(str(res) + '\n')

    fptr.close()
