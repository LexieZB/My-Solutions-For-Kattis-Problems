n = int(input())
bracket_sequence = list(input())
stack = []
brackets = {'(': ')', '{': '}', '[': ']'}
# print(bracket_sequence)
for i in bracket_sequence:
    stack.append(i)
    l = len(stack)
    if l >= 2:
        #print(stack[l-1])
        #print(stack[l-2])
        if stack[l-2] in brackets:
            if stack[l-1] == brackets[stack[l-2]]:
                stack.pop()
                stack.pop()

check = len(stack)
if check == 0:
    print('Valid')
else:
    print('Invalid')
