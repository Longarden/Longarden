n = int(input())
sen = ""


# Please write your code here.
def square(a):
    num = 1
    for i in range(a):
        for j in range(a):
            if (num==10):
                num = 1
            print(num, end=" ")
            num += 1
        print()


square(n)
