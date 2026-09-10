n = int(input())
# false表示灯关，true表示灯开，按一次开关用not把状态反过来
lights = [False] * 2000001  # 列表从0开始到2000000，需要2000001个位置
for i in range(n):
    a,t = input().split()
    a = float(a)
    t = int(t)
    for k in range(1, t + 1):
        number = int(k * a)
        lights[number] = not lights[number]
for number in range(1, 2000001):  # 不从0开始，是因为题目灯编号是从1开始
    if lights[number] == True:
        print(number)
        break  # 题目保证最后只有一盏灯开着。找到并输出以后，就不需要继续检查后面的灯了，因此使用 break 结束循环。


