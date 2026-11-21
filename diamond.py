n=5
#upper half

for i in range (1,n+1) : 
    # j is for the spaces
    for j in range (n-i) : 
        print(" ",end="")
    for k in range (2*i-1) : 
        print("*",end="")
    print()

#lower half

for i in range(n-1,0,-1) : 
    for j in range (n-i) : 
        print(" ",end="")
    for k in range (2*i-1) : 
        print("*",end="")
    print()