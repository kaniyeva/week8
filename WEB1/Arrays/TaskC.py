n=int(input())
count=0
a=[int(i) for i in input().split()]
for i in a:
    if i>0:
        count+=1
print(count)