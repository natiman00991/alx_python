def print_combinations():
    for i in range(10):
        for j in range(i + 1, 10):
            if i != j:
                print("{0:02d},{1:02d}, ".format(10 * i + j, 10 * j + i), end="")
    print()


print_combinations()
