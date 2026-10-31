#                              prime fectors

def prime_fectors(n):
    prime = []
    i = 2

    while i <= n:
        if n % i == 0:
            prime.append(i)
            n //= i
        else:
            i += 1

    print(prime)


prime_fectors(12)

    