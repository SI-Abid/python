def get_prime() -> int:
    """
    Returns the next prime number.
    """
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

def is_prime(n: int) -> bool:
    """
    Returns True if n is prime.
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# 25th prime number
cnt = 1
for p in get_prime():
    print(cnt, p)
    if cnt == 25:
        break
    cnt += 1