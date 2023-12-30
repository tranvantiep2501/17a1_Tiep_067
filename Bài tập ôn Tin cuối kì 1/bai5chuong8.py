n = int(input('Nhập số năm : '))
for i in range(1, n + 1 ):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0 : 
        print(i , 'là năm nhuận')
    else: 
        print(i, 'không là năm nhuận')

# cách khác 
nam = int(input('Nhập số năm : '))
if nam % 4 == 0 and nam % 100 != 0 or nam % 400 == 0 :
    print(nam, 'là năm nhuận')
else: 
    print(nam, 'không phải là năm nhuận ')
    