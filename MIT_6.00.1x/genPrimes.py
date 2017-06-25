def isPrime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def genPrimes():
    p = 2
    while True:
        if isPrime(p):
            yield p
        p += 1