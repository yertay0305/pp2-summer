import math 

n = int(input("n="))
l = int(input("l="))
tan = math.tan(math.radians(180/n))
area = n * l ** 2 / (tan * 4)
print("Area: ", int(area))