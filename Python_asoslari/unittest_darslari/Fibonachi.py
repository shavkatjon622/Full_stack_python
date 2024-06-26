def fibonacci(n):
    """Berilgan son fibonacci ketma-ketligida bor yoki yo`qligini tekshiruvchi funksiya"""
    fib = [0, 1]
    sanoq = 0
    while n > fib[-1]:
        yangi = fib[sanoq] + fib[sanoq+1]
        fib.append(yangi)
        sanoq += 1
    if n in fib:
        return True
    else:
        return False
