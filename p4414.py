# P4414 [COCI 2006/2007 #2] ABC
# 时间限制: 1.00s    内存限制: 125.00MB
# 题目描述
# 三个整数分别为 A,B,C。这三个数字不会按照这样的顺序给你，但它们始终满足条件：A<B<C。为了看起来更加简洁明了，我们希望你可以按照给定的顺序重新排列它们。
#
# 输入格式
# 第一行包含三个正整数 A,B,C，不一定是按这个顺序。这三个数字都小于或等于 100。第二行包含三个大写字母 A、B 和 C（它们之间没有空格）表示所需的顺序。
#
# 输出格式
# 在一行中输出 A，B 和 C，用一个 （空格）隔开。
# 输入输出样例
# 输入
# 1 5 3
# ABC
# 输出
# 1 3 5
#
# 输入
# 6 4 2
# CAB
# 输出
# 6 2 4
# #include <iostream>
# #include <algorithm>
# #include <vector>
# #include <map>
# #include <string>
# using namespace std;
# int main()
# {
#     int a,b,c;
#     cin>>a>>b>>c;
#     string order;
#     cin>>order;
#     // 将三个整数存入数组并排序
#     vector<int>nums={a,b,c};
#     sort(nums.begin(),nums.end());
#      // 创建映射：A->最小值, B->中间值, C->最大值
#     map<char,int> numsMap;
#     numsMap['A']=nums[0];
#     numsMap['B']=nums[1];
#     numsMap['C']=nums[2];
#     //根据顺序字符串输出结果
#     for(int i=0;i<order.size();i++)
#     {
#         cout<<numsMap[order[i]];//输出当前数字
#          if (i < order.size() - 1) {  // 检查是否不是最后一个元素
#         cout << " ";  // 如果不是最后一个，添加空格
#     }
#     }
#     cout<<endl;
#     return 0;
# }
list = input().split()  # 例如输入cab input（）拿到的是"cab\n"
# .strip 去除首尾空白，把字符串开头和末尾所有看不见的空白字符（空格、换行符 \n、制表符 \t 等）全部删掉。

# 结合 input()，它的核心目的就是把末尾那个多余的“回车换行符”删掉，防止后面程序遍历的时候出错。
nums = []
for i in list:
    zheng = int(i)
    nums.append(zheng)
nums.sort()
zimu = input().strip()
result = []
for a in zimu:
    if a == 'A':
        result.append(nums[0])
    elif a == 'B':
        result.append(nums[1])
    else:
        result.append(nums[2])
print(*result)
# 最后输出时不要用 join，直接解包打印，Python 内部会自动帮你处理转换成文字
# print(*result) 的意思是把列表里的东西拆开打印，中间默认用空格隔开

