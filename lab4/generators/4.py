def square_number_generator(a, b):
    for a in range(a, b+1):
        yield a ** 2

a_str = input("a=")
b_str = input("b=")
a = int(a_str)
b = int(b_str)
for square in square_number_generator(a, b):
    print (square)