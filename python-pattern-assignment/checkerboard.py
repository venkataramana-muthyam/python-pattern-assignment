def checkerboard(size):
    for i in range(size):
        for j in range(size):
            if (i + j) % 2 == 0:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print()
checkerboard(5)