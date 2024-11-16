fibonacci = [0, 1]


def fibo(value):
    for i in range(1, value):
        fibonacci[1], fibonacci[0] = fibonacci[1] + fibonacci[0], fibonacci[1]
    return fibonacci[1]


fibo_input = int(input())
print(fibo(fibo_input))
