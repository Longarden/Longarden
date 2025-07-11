def okay(n):
    a=n%10
    b=n//10
    if n%2==0:
        if (a+b)%5==0:
            return True
    else: return False


n = int(input())

if okay(n):
    print("Yes")
else:
    print("No")