from math import sqrt

a, b, c = map(int, input('Nhập 3 cạnh a, b, c : ').split())
if a + b > c and a + c > b and c + b > a: 
    print('Đây là tam giác')
    p =  (a + b + c) / 2 
    print('Nửa chu vi của tam giác là :', p)
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print('Diện tích của tam giác là :', s)
else: 
    print('Xin hãy nhập lại vì không thể tạo thành 1 tam giác!!!')
    