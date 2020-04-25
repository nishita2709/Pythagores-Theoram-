n=int(input("Enter the no. of inputs you want:"))
for k in range(n):
    m=int(input("Enter the no.:"))
    for i in range(0,m+1):
        for j in range(0,m+1):
            if(i<=j):
                a=m
                b=i*i+j*j
                if(a==b):
                    print("(",i,",",j,")")
