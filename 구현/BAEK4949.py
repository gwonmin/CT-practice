s_lst = []
while True:
    inp = input()
    if inp == '.':
        break
    else:
        s_lst.append(inp)

for s in s_lst:
    stack = ''
    for i in s:
        if i == '(' or i == ')' or i == '[' or i == ']':
            stack += i

    tf = True
    while tf:
        ori_len = len(stack)
        stack = stack.replace('[]','').replace('()','').strip()
        new_len = len(stack)
        if ori_len == new_len:
            tf = False

    if '(' in stack or ')' in stack or '[' in stack or ']' in stack:
        print('no')
    else:
        print('yes')