a = [int(i) for i in input().split()]
if a[0] + a[1] == a[2]: print(a[0],'+',a[1],'=',a[2],sep="")
elif a[0] - a[1] == a[2]: print(a[0],'-',a[1],'=',a[2],sep="")
elif a[0] * a[1] == a[2]: print(a[0],'*',a[1],'=',a[2],sep="")
elif a[0] / a[1] == a[2]: print(a[0],'/',a[1],'=',a[2],sep="")
elif a[0] == a[1] + a[2]: print(a[0],'=',a[1],'+',a[2],sep="")
elif a[0] == a[1] - a[2]: print(a[0],'=',a[1],'-',a[2],sep="")
elif a[0] == a[1] * a[2]: print(a[0],'=',a[1],'*',a[2],sep="")
elif a[0] == a[1] / a[2]: print(a[0],'=',a[1],'/',a[2],sep="")
