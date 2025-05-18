n, m = map(int, input().split())
num=2
ans=[]
# Please write your code here.
while(True):
    if n%num==0 and m%num ==0:
        ans.append(num)
    num+=1
    if num>n:
        break
ans.sort()
ans.reverse()
print(ans[0])
num=2