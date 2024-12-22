def abc(n):
    iteration= 0
    for i in range(0,n):
        for p in range(0,n):
            print("*",end="")
            iteration= iteration+1
        print("")
    print(iteration)
abc(10)