y = int(input())

# Please write your code here.
def Year(n):
    if(n%100==0 and n%400!=0):return False
    if(n%4==0):
        return True
    return False
if(Year(y)):print("true")
else: print("false")