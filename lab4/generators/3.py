def divisible_number_generator(n):
    for i in range(n+1):
        if i % 3 == 0:
            if i % 4 == 0:
                yield i 

n_str = input("n=")
n = int(n_str)
for divisible in divisible_number_generator(n):
    print(divisible)