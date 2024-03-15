stack = []
text = ''
n = int(input())
for i in range(n):
    cmd = input()
    if cmd[0] == '1':
        stack.append(text)
        text += cmd[2:]
    elif cmd[0] == '2':
        stack.append(text)
        k = int(cmd[2:])
        text = text[:-k]
    elif cmd[0] == '3':
        k = int(cmd[2:])
        print(text[k - 1])
    else:
        text = stack.pop()

    # print(stack)
