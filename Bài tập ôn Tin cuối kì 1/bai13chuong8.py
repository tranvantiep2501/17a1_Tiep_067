# Tổng các số lẻ nhỏ hơn hoặc bằng n 
n = int(input('Nhập một số n : '))
tong = 0 
i = 1 
while i <= n: 
    if i % 2 == 1 : 
        tong += i 
    i += 1
print(f'TỔng là {tong}')

# Tổng các số chẵn nhỏ hơn hay bằng n 
n = int(input('NHập một số n : '))
tong = 0 
i = 1 
while i <= n : 
    if i % 2 == 0: 
        tong += i 
    i += 1
print(f'Tổng là {tong}')

#Tích các số từ 1 đến n 
n = int(input('NHập một số n : '))
tich = 1
for i in range(1, n + 1): 
    tich *= i
print(f'Tích là {tich}')

#Tích các số chia hết cho 3 nhỏ hơn hay bằng n 
n = int(input('NHập n : '))
tich = 1 
i = 1
while i <= n : 
    if i % 3 == 0 : 
        tich *= i
    i += 1 
print(f'Tích là {tich}')

#Tổng các số nguyên tố nhỏ hơn hay bằng n 
n = int(input('Nhập n : '))
tong = 0 
i = 1 
while i <= n : 
    if i > 2 :
        is_nto = True 
        for i in range(2, n + 1 ):
            if i % 2 == 0 : 
                break
                is_nto = False
        tong += i 
    i += 1
print(f'TỔng là {tong}')
        


















