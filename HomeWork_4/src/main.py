import time

def simplePrimeSearch(n: int) -> dict[int, bool]:
    primes = {}

    for number in range(2, n + 1):
        is_prime = True
        d = 2
        while d * d <= number:
            if number % d == 0:
                is_prime = False
                break
            d += 1

        primes[number] = is_prime

    return primes

def sieveEratosthenes(n: int) -> dict[int, bool]:
    primes = {}

    for i in range(2, n + 1):
        primes[i] = True
    i = 2
    while i * i <= n:
        if primes[i]:
            j = i * i
            while j <= n:
                primes[j] = False
                j += i
        i += 1

    return primes

def measureTime(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    elapsed = end - start
    print(f"Time of the {func.__name__} function: {elapsed:.10f} sec.")
    return result, elapsed

def countPrimes(primesDict: dict[int, bool]) -> int:
    return sum(primesDict.values())

def main():
    limits = [100, 1000, 10000]

    for n in limits:
        print(f"\nSearch primes up to {n}")
        primesSimple, timeSimple = measureTime(simplePrimeSearch, n)
        primesSieve, timeSieve = measureTime(sieveEratosthenes, n)
        print("Primes found (simple):", countPrimes(primesSimple))
        print("Primes found (sieve) :", countPrimes(primesSieve))
        if timeSieve > 0:
            print(f"Sieve is faster ~ {timeSimple / timeSieve:.2f}x")

if __name__ == "__main__":
    main()


'''Висновок.
У роботі було реалізовано два методи пошуку простих чисел: простий перебір дільників та більш ефективний алгоритм — решето Ератосфена. 
За допомогою вимірювання часу виконання було встановлено, що при збільшенні діапазону пошуку решето Ератосфена працює значно швидше за наївний метод. 
Це підтверджує доцільність використання ефективних алгоритмів для обробки великих обсягів даних.'''