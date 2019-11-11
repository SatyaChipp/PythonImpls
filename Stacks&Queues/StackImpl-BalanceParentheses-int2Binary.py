"""
1.Stack
LIFO
 D
 C
 B
 A

2.Determine whether a set of parenthesis are balanced or not

3.Convert integer to binary
"""


"""
1.Stack
LIFO
 D
 C
 B
 A
"""
class Stack(object):
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self, item=None, index=None): ##item and index not needed for stacks
        return self.items.pop()
    def get_stack(self, sideBySide=0):
        if not sideBySide:
            return '\n'.join(self.items)
        else:
            return ''.join(self.items)
    def reverse_stack(self, sideBySide=0):
        if not sideBySide:
            return '\n'.join(self.items[::-1])
        else:
            return ''.join(self.items[::-1])

    def is_empty(self):
        return bool(len(self.items)==0)
    def peek(self):
        if self.is_empty():
            return self.items[-1]
        else:
            return 'Empty Stack'
    def size(self):
        return len(self.items)

"""
2.Determine whether a set of parenthesis are balanced or not
"""
input = "{]]]{{{{[]{()}})"
input_bal = "{[{(}}])"
def check_balance_paranthesis_nonSequence(inp):
    open_par = ['[', '{', '(']
    close_par = [']', '}', ')']
    queue = []
    from collections import Counter
    par_counter = Counter(inp)
    zipp = dict(zip(open_par, close_par))
    for key, value in zipp.items():
        if par_counter[key] == par_counter [value]:
            pass
        else:
            return 'unbalanced'
    return 'balanced'


def check_balance_paranthesis_using_stacks_parensInSequence(inp):
    s=Stack()
    is_balanced = True #set flag to truw
    index = 0
    def is_match(p1, p2):
        if p1 == '(' and p2 == ')':
            return True
        elif p1 == '{' and  p2=='}':
            return True
        elif p1 == '(' and  p2==')':
            return True
        else:
            return False

    while index < len(inp) and is_balanced: #loop through the string
        paren = inp[index]
        if paren in '({[': #is char in open parens
            s.push(paren)
        else:
            if s.is_empty(): #is is empty we already know it isnt balanced
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced=False
        index+=1
    if is_balanced and s.is_empty():
        return 'balanced'
    else:
        return 'unbalanced'

"""
3.Convert integer to binary
"""
def convert_interger_toBinary(intnum):
    s = Stack()
    quo = 1
    if isinstance(intnum, int):
        while quo !=0:
            quo, rem = divmod(intnum, 2)
            s.push(str(rem))
            intnum=quo
    return s.reverse_stack(sideBySide=1)


if __name__ == '__main__':
    s = Stack()
    s.push('A')
    s.push('B')
    s.push('G')
    print(s.get_stack(sideBySide=1))
    print(s.reverse_stack(sideBySide=1))
    print(s.pop())
    print(s.is_empty())
    print(check_balance_paranthesis_nonSequence(input_bal))
    print(check_balance_paranthesis_using_stacks_parensInSequence(input_bal))
    print(convert_interger_toBinary(125123))

    
 OUTPUT """
 ABG
GBA
G
False
balanced
unbalanced
11110100011000011
  """





