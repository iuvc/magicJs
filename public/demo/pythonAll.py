# 2011 测试题一 =================================分值：30 列阵分数总和

# n,m = map(int,input().split())
# a = []
# for i in range(n):
#     li = list(map(int,input().split()))
#     a.append(li)
# for j in range(m):
#     s = 0
#     for i in range(n):
#         s+= a[i][j]
#     print(s,end=" ")

# 1911 测试题二 =================================分值：20 小鱼眼里可爱

# n = int(input())
# a = list(map(int,input().split()))
# for i in range(n):
#     k = 0
#     for j in range(i):
#         if a[j]<a[i]:
#             k += 1
#     print(k , end=' ')

# 1511 测试题三 =================================分值：50 Alice倒茶

# n,k,l = map(int,input().split())
# s = list(map(int,input().split()))
# s.sort()
# t = 0
# for i in range(k):
#     t+=s[i]
# print((t+l-1)//l)

# 1011 测试题四 =================================分值：20 小翔迷宫

# n = int(input())
# s = input()
# t = 0
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         s1 = s[i:j+1]
#         u,d,l,r = 0,0,0,0
#         for q in s1:
#             if q=='U':
#                 u+=1
#             if q=='D':
#                 d+=1
#             if q=='L':
#                 l+=1
#             if q=='R':
#                 r+=1
#         if u==d and l==r:
#             t+=1
# print(t)

# 0611 测试题五 =================================分值：50 纸牌游戏

# n = int(input())
# li = list(map(int,input().split()))
# avg = sum(li) / n
# moveN = 0
# for i in range(n-1):
#     if li[i]!=avg:
#         li[i+1]+=li[i]-avg
#         moveN+=1
# print(moveN)

# 1411 测试题六 =================================分值：30 三色牌

# n = int(input())
# s = input()
# r,g,b = 0,0,0
# for t in s:
#     if t=='B':
#         b+=1
#     if t=='G':
#         g+=1
#     if t=='R':
#         r+=1
# if b==n:
#     print('B')
# elif g==n:
#     print('G')
# elif r==n:
#     print('R')
# else:
#     if b!=n-1:
#         print('B',end='')
#     if g!=n-1:
#         print('G',end='')
#     if r!=n-1:
#         print('R',end='')

# 0411 测试题七 =================================分值：20 数字排序

# a = list(map(int,input().split()))
# x = int(input())
# a.insert(9,x)
# a.sort()
# for n in a:
#     print(n)
# print()

# 0111 测试题八 =================================分值：20 完数因子

# from math import sqrt
# while 1:
#     n = int(input())
#     print(n,':',sep='',end='')
#     for i in range(6,n+1):
#         t=1
#         for j in range(2,int(sqrt(i)+1)):
#             if i%j==0:
#                 t=t+j+i/j
#         if t==i:
#             print('',i,end='')
#     print()

# 0911 测试题九 =================================分值：50 六一彩灯游戏

# n = int(input()) # n,表示有n盏灯，n<=100
# a = [0]*n
# y = ['white','red','yellow', 'blue']
# b = [0, 0, 0, 0]
# maxN,cnt,index = 0,0,0
# while True:
#     try:
#         m=int(input())
#         a[m-1] = (a[m-1]+1)%4
#     except:
#         break
# for i in a:
#     b[i]+=1
#     if b[i]>maxN:
#         maxN = b[i]
#         index = i
# for t in b:
#     if t==maxN:
#         cnt+=1
# if cnt==1:
#     print(y[index],maxN)
# else:
#     print(maxN)

# 0511 测试题十 =================================分值：30 珠心算

# n = input().split()
# l = input().split()
# s = set(l)
# l = list(s)
# ans = set(l)
# cnt = 0
# ans.clear()
# for i in range(0,len(l)):
#     x = int(l[i])
#     for j in range(i+1,len(l)):
#         y = int(l[j])
#         if str(x+y) in s:
#             if str(x+y) in ans:
#                 continue
#             else:
#                 cnt+=1
#                 ans.add(str(x+y))
# print(len(ans))

# 1611 测试题十一 =================================分值：20 --》偶数和

# x = int(input())
# s = 0
# while x>0:
#     k=x%10
#     x=x//10
#     if k%2==0:
#         s+=k
# print(s)

# 0811 测试题十二 =================================分值：30 --》画太阳

# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
# def search(a,x,y):
#     a[x][y] = '0'
#     for i in range(4):
#         x1 = x+dx[i]
#         y1 = y+dy[i]
#         if 0<=x1<r and 0<=y1<w and a[x1][y1]=='1':
#             search(a,x1,y1)
# n = int(input())
# for i in range(n):
#     r,w = map(int,input().split())
#     a = []
#     cnt = 0
#     for j in range(r):
#         a.append(list(input()))
#     for j in range(r):
#         for k in range(w):
#             if a[j][k]=='1':
#                 cnt+=1
#                 search(a,j,k)
#     print(cnt)

## 示例输入===》
## 1
## 4 5
## 01000
## 10011
## 10011
## 00000
## 输出===》
## 3

# 1211 测试题十三 =================================分值：50 --》张小杰CF

# n = int(input())
# s = list(map(int,input().split()))
# t = 0
# if s[0] == 0:
#     t+=1
# for i in range(1,n):
#     if s[i]==0:
#         t+=1
#     if s[i]==1 and s[i-1]==1:
#         t+=1
#         s[i] =0
#     if s[i]==2 and s[i-1]==2:
#         t+=1
#         s[i]==0
#         if s[i]==3:
#             if s[i-1]==1:
#                 s[i]=2
#             if s[i-1]==2:
#                 s[i]=1
# print(t)

# 1811 测试题十四 =================================分值：50 --》棋盘指令

# n = int(input())
# for i in range(n):
#     str = input()
#     w,a,s,d =0,0,0,0
#     for c in str:
#         if c=='w':
#             w+=1
#         if c=='a':
#             a+=1
#         if c=='s':
#             s+=1
#         if c=='d':
#             d+=1
#     if w<s:
#         minws = w
#     else:
#         minws = s
#     if a<d:
#         minad = a
#     else:
#         minad = d
#     if minws ==0:
#         if minad==0:
#             print(0)
#         else:
#             print(2)
#     else:
#         if minad==0:
#             print(2)
#         else:
#             print(2*(minad+minws))

# 1711 测试题十五 =================================分值：30 --》元旦新年晚会

# w = int(input())
# n = int(input())
# a = []
# for i in range(n):
#     x = int(input())
#     a.append(x)
# b = sorted(a)
# l = 0
# r = n-1
# ans = 0
# while l<=r:
#     if b[l]+b[r]<w:
#         l+=1
#     r-=1;
#     ans+=1
# print(ans)

## 示例输入===》
## 100 #上限
## 9 # 个数
## 20 # 具体每个数值，下同
## 90
## 20
## 30
## 50
## 60
## 70
## 80
## 90
## 输出===》
## 6

# 0211 测试题十六 =================================分值：30 --》牛牛日期

# date1 = int(input())
# date2 = int(input())
# year1 = date1 // 10000
# year2 = date2 // 10000
# n = 0
# for i in range(year1,year2+1):
#     x = int(str(i)[::-1])
#     if i== (year1 or year2):
#         temp = i*10000+x
#         if temp<date1 or temp>date2:
#             continue
#     month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
#     if (i%400 == 0) or (i%4==0 and i%100 !=0):
#         month[2]+= 1
#     if x%100 > 31 or x // 100 >12:
#         continue
#     elif x%100>month[x//100]:
#         continue
#     else:
#         n+=1
# print(n)

## 示例输入===》
## 20110101
## 20111231
## 输出===》
## 1

# 1311 测试题十七 =================================分值：20 --》哥德巴赫猜想

# def prime(x):
#     for i in range(2,x):
#         if x%i == 0:
#             return False
#     return True
# def demo():
#     n = eval(input())
#     while n<5 or n%2!=0:
#         n = eval(input())
#     for i in range(2,n//2+1):
#         if prime(i) and prime(n-i):
#             print(n,'=',i,'+',n-i)
#             break
# demo()

## 示例输入===》
## 3
## 9
## 8
## 输出===》
## 8 = 3 + 5

# 0711 测试题十八 =================================分值：20 --》反向关灯

# n,m = input().split()
# n = int(n)
# m = int(m)
# a = []
# b = []
# c = []
# for i in range(n):
#     a.append(1)
# for i in range(1,m+1):
#     b.append(i)
# for i in b:
#     for i in range(i-1,n,i):
#         a[i] = 1-a[i] # 与自己倍数同等做相反处理
# for i in range(n):
#     if a[i]==0:
#         c.append(i+1)
#         c.append(',')
# for i in range(len(c)-1):
#     print(c[i],end='')
    
## 示例输入===》
## 10 10
## 输出===》
## 1,4,9

# 1111 测试题十九 =================================分值：30 --》红蓝纸牌

# a,b = map(int,input().split())
# t1 = [0]*5
# t2 = [0]*5
# for i in range(1,a+1):
#     t1[i%5]+=1
# for i in range(1,b+1):
#     t2[i%5]+=1
# print(t1[0]*t2[0]+t1[1]*t2[4]+t1[2]*t2[3]+t1[3]*t2[2]+t1[4]*t2[1])
    
## 示例输入===》
## 6 12
## 输出===》
## 14

# 0311 测试题二十 =================================分值：未知 --》民意调查

# from math import gcd
# a,b,l = map(int,input().split())
# ans1 = l
# ans2 = 1
# for i in range(1,l):
#     for j in range(1,l):
#         if(gcd(i,j)==1 and i*b>=j*a and i*ans2<j*ans1):
#             ans1 = i
#             ans2 = j
# print(ans1,ans2)
    
## 示例输入===》
## 1498 902 1501
## 输出===》
## 749 451