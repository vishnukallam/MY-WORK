T = int(input("Enter a number : "))
for i in range(T):
    H, X, Y = map(int, input("enter three numbers by giving spaces: ").split())
    # hits_required = H // (X + Y)
    if H % (X + Y) == 0:
        print("1")
    else:
        print("0")
