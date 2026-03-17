import time

def Fibonacci_再帰(n):
    if(n == 0):
        return 0
    if(n == 1 or n == 2):
        return 1
    
    return Fibonacci_再帰(n - 1) + Fibonacci_再帰(n-2)

def Fibonacci_サイクル(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


start = time.perf_counter()
print(Fibonacci_再帰(12))
end = time.perf_counter()

print(f"再帰: {(end - start) * 1000}ミリ秒")


start = time.perf_counter()
print(Fibonacci_サイクル(12))
end = time.perf_counter()

print(f"サイクル: {(end - start) * 1000}ミリ秒")