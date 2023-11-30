def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} is not prime")
            return False
    print(f"{n} is prime")
    return True


DEFAULT_NUMBERS = [1297337, 1116281, 104395303, 472882027,
                   533000389, 817504243, 982451653,
                   112272535095293, 115280095190773, 1099726899285419] * 20
