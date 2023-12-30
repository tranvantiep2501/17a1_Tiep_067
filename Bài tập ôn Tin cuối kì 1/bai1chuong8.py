# CÒN CÁCH KHÁC NẾU MUỐN NHẬP TỪ BÀN PHÍM : TA DÙNG map(int, input('').split())
a = int(input('Nhập a :'))
b = int(input('Nhập b : '))
c = int(input('Nhập c :'))
d = int(input('Nhập d : '))
if a > b and a > c and a > d:
    print('a = ', a, 'là max')
    if b < c and b < d :
        print('b = ', b, 'là min')
    if c < b and c < d:
        print('c =', c, 'là min')
    if d < c and d < b:
        print('d =', d, 'là min')
if b > a and b > c and b > d:
    print('b = ', b, 'là max')
    if a < c and a < d : 
        print('a = ', a, 'là min')
    if c < a and c < d:
        print('c = ', c, 'là min')
    if d < a and d < c:
        print('d =', d, 'là min')
if c > a and c > b and c > d:
    print('c =', c, 'là max ')
    if a < b and a < d : 
        print('a = ', a, 'là min')
    if b < a and b < d:
        print('b = ', b, 'là min')
    if d < a and d < b:
        print('d =', d, 'là min')
if d > a and d > b and d > c:
    print('d = ', d, 'là max')
    if a < c and a < b:
        print('a = ', a, 'là min ')
    if b < c and b < a: 
        print('b = ', b, 'là min')
    if c < a and c < b:
        print('c =', c, 'là min')