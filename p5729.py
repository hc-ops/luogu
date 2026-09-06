# # P5729 【深基5.例7】工艺品制作
#
# ## 题目描述
#
# 现有一个长宽高分别为 $w,x,h$ 组成的实心玻璃立方体，可以认为是由 $1\times1\times1$ 的数个小方块组成的，每个小方块都有一个坐标 $ ( i,j,k ) $。现在需要进行 $q$ 次切割。每次切割给出 $(x_1,y_1,z_1),(x_2,y_2,z_2)$ 这 6 个参数，保证 $x_1\le x_2$，$y_1\le y_2$，$z_1\le z_2$；每次切割时，使用激光工具切出一个立方体空洞，空洞的壁平行于立方体的面，空洞的对角点就是给出的切割参数的两个点。
#
# 换句话说，所有满足  $x_1\le i\le x_2$，$y_1\le j \le y_2 $，$z_1\le k\le z_2$ 的小方块 $(i,j,k)$ 的点都会被激光蒸发。例如有一个  $4\times4\times 4$ 的大方块，其体积为 $64$；给出参数 $(1,1,1),(2,2,2)$ 时，**对应的** $8$ 块小方块就会被蒸发，剩下 $56$ 个小方块。现在想知道经过所有切割操作后，剩下的工艺品还剩下多少格小方块的体积？
#
# ## 输入格式
#
# 第一行三个正整数 $w,x,h$。
#
# 第二行一个正整数 $q$。
#
# 接下来 $q$ 行，每行六个整数 $(x_1,y_1,z_1),(x_2,y_2,z_2)$。
#
# ## 输出格式
#
# 输出一个整数表示答案。
#
# ## 输入输出样例 #1
#
# ### 输入 #1
#
# ```
# 4 4 4
# 1
# 1 1 1 2 2 2
#
# ```
#
# ### 输出 #1
#
# ```
# 56
# ```
#
# ## 说明/提示
#
# 数据保证，$1\le w,x,h\le 20$，$1 \leq q\le 100$。$1 \leq x_1 \leq x_2 \leq w$，$1 \leq y_1\leq y_2 \leq x$，$1 \leq z_1 \leq z_2 \leq h$。
w,x,h=input().split()
w=int(w)
x=int(x)
h=int(h)
q=int(input())
removed=[False]*(w*x*h)#创建一个列表，里面内容是w*x*h个false,false表示小方块没有蒸发掉
answer=w*x*h#小方块总量
for _ in range(q):
    x1,y1,z1,x2,y2,z2=input().split()
    x1=int(x1)
    y1=int(y1)
    z1=int(z1)
    x2=int(x2)
    y2=int(y2)
    z2=int(z2)
    #注意两端都包含，所以一次蒸发的小方块数量是：
#(x2-x1+1)(y2-y1+1)(z2-z1+1)
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            for k in range(z1,z2+1):
                #将三维坐标转换成一维列表下标
                number=(i-1)*h*x+(j-1)*h+(k-1)
                #因为列表下标初始为0，坐标初始为1，所以减1
                if removed[number]==False:
                    removed[number]=True
                    answer=answer-1
print(answer)
