# # P1307 [NOIP 2011 普及组] 数字反转
#
# ## 题目描述
#
# 给定一个整数 $N$，请将该数各个位上数字反转得到一个新数。新数也应满足整数的常见形式，即除非给定的原数为零，否则反转后得到的新数的最高位数字不应为零（参见样例 2）。
#
# ## 输入格式
#
# 一个整数 $N$。
#
# ## 输出格式
#
# 一个整数，表示反转后的新数。
#
# ## 输入输出样例 #1
#
# ### 输入 #1
#
# ```
# 123
# ```
#
# ### 输出 #1
#
# ```
# 321
# ```
#
# ## 输入输出样例 #2
#
# ### 输入 #2
#
# ```
# -380
# ```
#
# ### 输出 #2
#
# ```
# -83
# ```
#
# ## 说明/提示
#
# **【数据范围】**
#
# $-1,000,000,000\leq N\leq 1,000,000,000 $。
#
# noip2011 普及组第一题
# #include<bits/stdc++.h>
# using namespace std;
# int main()
# {
#     long long N;
#     cin>>N;
#         bool isNegative = (N < 0);  // 判断 N 是否为负数：若 N < 0 则 isNegative = true，否则 false
#     if (isNegative) {           // 如果 N 是负数
#         N = -N;                 // 取绝对值（例如 -380 → 380），方便后续反转
#     }
#     long long reversedNum=0;
#     while(N>0)
#     {
#         int lastDigit=N%10;
#         reversedNum=reversedNum*10+lastDigit;
#         N=N/10;
#     }
#     if(isNegative)
#     {
#         reversedNum=-reversedNum;
#     }
#     cout<<reversedNum<<endl;
#     return 0;
# }
N=int(input())
if N<0:
    N=str(-N)
    pal=-int(N[::-1])
    print(pal)
else:
    N=str(N)
    pal=int(N[::-1])
    print(pal)