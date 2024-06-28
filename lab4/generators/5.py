def reverse_generator(n):
    while n >= 0:
        yield n
        n -= 1

n_str = input("n=")
n = int(n_str)
for reverse in reverse_generator(n):
    print(reverse)