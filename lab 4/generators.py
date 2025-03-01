# task 1
def squares_up_to(n):
    for i in range(n+1):
        yield i * i

# task 2
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter n: "))
print(",".join(map(str, even_numbers(n))))

# task 3
def div_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# task 4 
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

for num in squares(2, 5):  
    print(num)

# task 5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

for num in countdown(5): 
    print(num)
