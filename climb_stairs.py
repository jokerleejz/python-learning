def climb_stairs_1(n):
    # 迭代
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_stairs_1(n-1) + climb_stairs_1(n-2)


def climb_stairs_2(n):
    # 动态规划
    if n == 1:
        return 1
    if n == 2:
        return 2
    a, b, i = 1, 2, 3
    while i <= n:
        a, b = b, a+b
        i += 1
    return b


if __name__ == '__main__':
    print(climb_stairs_1(10))
    print(climb_stairs_2(10))
