def squares_generator(n):
    for i in range(n+1):
        yield i**2

n_str = input("n=")
n = int(n_str)
for square in squares_generator(n):
    print(square)