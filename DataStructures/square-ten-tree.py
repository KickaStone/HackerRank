import math
import sys

ans = []
sys.set_int_max_str_digits(0) # 2

def process(l, r, level, ans):
    if level == 0:
        # ans[0] += r - l + 1
        ans.append((0, r - l + 1))
        # print('single', l, r)
        return
    if level < 0:
        return
    # print(f'processing l = {l}, r = {r}, level={level}')
    step = int(10 ** (2 ** (level - 1)))
    start = (l - 1) // step * step
    # if l % step == 1:
    #     start = l
    # else:
        # start = (l // step + 1) * step + 1
    start = (l + step - 2) // step * step + 1
    end = r // step * step
    # print(f'start = {start}, end = {end}, step = {step}')
    # if l == r:
    #     # if level == 0:
    #     #     print(l)
    #     # ans[0] += 1
    #     ans.append(())
    #     return
    if start > end:
        process(l, r, level - 1, ans)
    else:
        if l < start:
            process(l, start-1, level - 1, ans)

        cnt = (end - start + 1) // step
        # ans[level] += cnt
        ans.append((level, cnt))
        # print(start, end, cnt)

        if r > end:
            process(end+1, r, level - 1, ans)
def get_top_level(n):
    if n <= 1:
        return 0
    return int(math.log2(math.log10(n))) + 1


if __name__ == '__main__':
    l = int(input())
    r = int(input())
    # l, r = 1, 101
    # f = open('input33.txt')
    # l = int(f.readline())
    # r = int(f.readline())

    # print(data)
    f.close()

    # l = 90200
    # r = 8709800060
    res = []
    sum_ = r - l + 1
    top = get_top_level(sum_)
    # ans = [0] * (top + 1)
    process(l, r, top, ans)

    # print(sum([True for n in ans if n > 0]))
    print(len(ans))
    for pack in ans:
        print(pack[0], pack[1])


# TLE
