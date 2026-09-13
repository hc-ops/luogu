# # P5731 【深基5.习6】蛇形方阵
#
# ## 题目描述
#
# 给出一个不大于 $9$ 的正整数 $n$，输出 $n\times n$
# 的蛇形方阵。
#
# 从左上角填上 $1$ 开始，顺时针方向依次填入数字，如同样例所示。注意每个数字都会占用 $3$ 个字符，前面使用空格补齐。
#
# ## 输入格式
#
# 输入一个正整数 $n$，含义如题所述。
#
# ## 输出格式
#
# 输出符合题目要求的蛇形矩阵。
#
# ## 输入输出样例 #1
#
# ### 输入 #1
#
# ```
# 4
# ```
#
# ### 输出 #1
#
# ```
#   1  2  3  4
#  12 13 14  5
#  11 16 15  6
#  10  9  8  7
# ```
#
# ## 说明/提示
#
# 数据保证，$1 \leq n \leq 9$。
n = int(input())
a = [[0] * n for _ in range(n)]  # 做 n 次循环；
# 每次生成一个 [0, 0, ..., 0]，长度是 n；
# 把这些行放进一个大列表 a 里。
# 所以 a 就是一个 n 行 n 列的二维列表。
bound = [0, n - 1, n - 1, 0]
top, right, bottom, left = bound  # 边界
num = 1  # 表示现在该填的数字
while num <= n * n:
    # 左上开始，top开始
    for j in range(left, right + 1):
        a[top][j] = num
        num += 1
    top += 1
    # 顺时针到右上，从right开始
    for i in range(top, bottom + 1):
        a[i][right] = num
        num += 1
    right -= 1
    # 继续顺时针到右下，从bottom开始
    for j in range(right, left - 1, -1):  # range(起点, 终点, 步长) -1位从右往左减
        a[bottom][j] = num
        num += 1
    bottom -= 1
    # 顺时针到左下，从left开始
    for i in range(bottom, top - 1, - 1):  # -1从下往上
        a[i][left] = num
        num += 1
    left += 1
for row in a:
    for x in row:
        print(f"{x:3d}", end="")  # 加上end="" 后，表示打印完不换行
    print()




