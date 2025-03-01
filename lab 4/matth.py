# task 1
import math

degree = float(input("Input degree: "))
radian = degree * (math.pi / 180)
print("Output radian:", round(radian, 6))

# task 2
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = 0.5 * (base1 + base2) * height
print("Expected Output:", area)

# task 3
import math

sides = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))

area = (sides * length**2) / (4 * math.tan(math.pi / sides))
print("The area of the polygon is:", round(area, 2))

# task 4
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height
print("Expected Output:", area)
