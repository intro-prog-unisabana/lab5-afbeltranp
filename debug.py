def find_max(a, b, c):          # BUG 1: faltaba el parámetro c
    max_number = a
    if a > b and a > c:
        max_number = a
    elif b > a and b > c:
        max_number = b
    else:
        max_number = c
    return max_number           # BUG 2: faltaba el return

#FREEZE CODE BEGIN
x = int(input("Enter a number:\n"))
y = int(input("Enter a number:\n"))
z = int(input("Enter a number:\n"))
#FREEZE CODE END

maximum = find_max(x, y, z)    # BUG 3: se llamaba con variables sin definir y no se almacenaba
print("Maximum value:", maximum)
