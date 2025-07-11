a, b = map(int, input().split())

def magic(n):
    if n%3==0:
        return True#3의 배수일떄
    # 하나들어간거
    for ch in str(n):
        if(ch in "369"):
            return True

cnt=0
for i in range(a,b+1):
    if(magic(i)): cnt+=1
print(cnt)