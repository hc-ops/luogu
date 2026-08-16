# # P1980 [NOIP 2013 普及组] 计数问题
#
# ## 题目背景
#
# NOIP2013 普及组 T1
#
# ## 题目描述
#
# 试计算在区间 $1$ 到 $n$ 的所有整数中，数字 $x$（$0\le x\le9$）共出现了多少次？例如，在 $1$ 到 $11$ 中，即在 $1,2,3,4,5,6,7,8,9,10,11$ 中，数字 $1$ 出现了 $4$ 次。
#
# ## 输入格式
#
# $2$ 个整数 $n,x$，之间用一个空格隔开。
#
# ## 输出格式
#
# $1$ 个整数，表示 $x$ 出现的次数。
#
# ## 输入输出样例 #1
#
# ### 输入 #1
#
# ```
# 11 1
# ```
#
# ### 输出 #1
#
# ```
# 4
# ```
#
# ## 说明/提示
#
# 对于 $100\%$ 的数据，$1\le n\le 10^6$，$0\le x \le 9$。
# #include<iostream>
# using namespace std;
# int main()
# {
#     int n,x;
#     cin>>n>>x;
#     int count=0;
#     for(int i=1;i<=n;i++)
#     {
#         int num=i;
#         while(num>0)
#         {
#             if(num%10==x){
#                 count++;
#             }
#             num/=10;
#         }
#     }
#     cout<<count<<endl;
#     return 0;
# }
n, x = input().split()
n = int(n)
x = int(x)
count = 0
for i in range(1, n + 1):
    num = i
    while num > 0:
        if num % 10 == x:
            count += 1
        num //= 10
print(count)
