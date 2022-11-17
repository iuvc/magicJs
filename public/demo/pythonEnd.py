
# 1911 测试题二 =================================分值：20 小鱼眼里可爱

# n = int(input())
# a = list(map(int,input().split()))
# for i in range(n):
#     k = 0
#     for j in range(i):
#         if a[j]<a[i]:
#             k += 1
#     print(k , end=' ')
    
## 示例输入===》
## 6 #小鱼条数
## 1 4 5 7 3 2 #各小鱼可爱值
## 输出===》
## 0 1 2 3 1 1 

# 1611 测试题十一 =================================分值：20 --》偶数和

# x = int(input())
# s = 0
# while x>0:
#     k=x%10
#     x=x//10
#     if k%2==0:
#         s+=k
# print(s)
    
## 示例输入===》
## 10345 #一串数字
## 输出===》
## 4


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
