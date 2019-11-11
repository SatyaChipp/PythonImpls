#### make sure the braces are paired

# Complete the braces function below.
def braces(values):
    opening = tuple('({[')
    closing = tuple(')}]')
    mapping = dict(zip(opening, closing))
    queue = []
    result = []
    def match_(item):
        for letter in item:
            if letter in mapping:
                queue.append(mapping[letter])
            elif not (queue and letter == queue.pop()):
                return False
        return not queue
    for item in values:
        if match_(item) is True:
            result.append('YES')
        else:
            result.append('NO')
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    values_count = int(input())

    values = []

    for _ in range(values_count):
        values_item = input()
        values.append(values_item)

    res = braces(values)

    fptr.write('\n'.join(res))
    fptr.write('\n')

    fptr.close()


#########################
INPUTS
#2
#{}[]()
#{[}]
#
#3
{[()]}
{[(])}
{{[[(())]]}}
#############3

