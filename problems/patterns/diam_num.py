def number_diamond_pattern(n):
    # Top half of the diamond
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    
    # Bottom half of the diamond
    for i in range(n - 1, 0, -1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

n = 5
number_diamond_pattern(n)
