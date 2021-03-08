def compute_hcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num 1 = 54
num 2 = 24

print('Nilai H.C.F adalah ',compute_hcf(num1, num2))