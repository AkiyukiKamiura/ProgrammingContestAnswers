#! python3
# fibonacci_number.py

fib_dic = {0:1, 1:1}
def fib(n):
    ans = fib_dic.get(n)
    if ans == None:
        fib_dic[n] = fib(n-1) + fib(n-2)
    return fib_dic[n]

n = int(input())
print(fib(n))
