import timeit


def modulo():
    r = 1000
    flag = 0

    for x in range(r):
        if x % 3 == 0 or x % 5 == 0:
            flag += 1

    print(f"Time taken for modulo:\t\t{timeit.timeit(lambda: flag)}")


def alternative():
    r = 1000
    flag = 0

    for x in range(r):
        if (x / 3).is_integer() or (x / 5).is_integer():
            flag += 1

    print(f"Time taken for alternative: {timeit.timeit(lambda: flag)}")


modulo()
alternative()
