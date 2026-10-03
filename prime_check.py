import math
def is_prime(num):
    if num == 1:
        return False
    count = 0
    for i in range(1, math.ceil(math.sqrt(num)) +1):
        if num % i == 0:
            count += 1
        if count > 1:
            return False

    return True

print(is_prime(3))
print(is_prime(4))
print(is_prime(13))
print(is_prime(11))