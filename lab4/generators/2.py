def even_number_generator(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n_str = input("n=")
n = int(n_str)
print (", ".join(map(str,even_number_generator(n))))