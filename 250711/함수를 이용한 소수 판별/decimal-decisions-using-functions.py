a, b = map(int, input().split())

# Please write your code here.
def fit(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

sum=0
for i in range(a,b+1):
    if(fit(i)):
        # print(i)
        sum+=i
print(sum)
