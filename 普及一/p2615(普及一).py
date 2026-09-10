#根据题目给出的要求，把四个规则简化一下
#如果右边越界，则直接从最后一列跳到第一列
#如果上方越界，则直接从第一行调到最后一行
#1.如果k-1在第一行且不在最后一列，则k的位置在k-1的右下方，画图即可
#2.如果k-1在最后一列但不在第一行，则k的位置在k-1的右上方，画图即可
#3.如果k-1在第一行最后一列，也就是右上，则k在k-1的正下方
#4.如果k-1既不在第一行也不在最后一列，则k优先填在k-1右上方，如果右上方有数则填到k-1的正下方
n=int(input())
magic=[]#创建n×n的二维列表，0表示这个位置还没有填数字
for i in range(n):
    line=[]
    for j in range(n):
        line.append(0)
    magic.append(line)
row=0#第一行
col=n//2#表示中间一列
magic[row][col]=1#把数字1放到row行，col列，也就是第一行的中间
for k in range(2,n*n+1):#依次产生需要填写的数字，并且每次进入循环时，row和col都会记录刚才填写k-1的位置，当准备写2，那么k-1=1，此时row和col记录的就是1的位置
    if row==0 and col!=n-1:
        row=n-1
        col=col+1
    elif col==n-1 and row!=0:
        row=row-1
        col=0
    elif row==0 and col==n-1:
        row=row+1
    else:
        if magic[row-1][col+1]==0:#先检查右上方是否有数字
            row=row-1
            col=col+1
        else:
            row=row+1
    magic[row][col]=k
for line in magic:
    print(*line)#依次取出二维列表的每一行
#* 的作用是把列表中的元素一个一个取出来。
#line = [8, 1, 6]，print(*line)=print(8,1,6)