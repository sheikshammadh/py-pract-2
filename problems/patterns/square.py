def square_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

n = 5
square_pattern(n)
