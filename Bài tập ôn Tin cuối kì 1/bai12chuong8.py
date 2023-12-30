so = int(input('Nhập một số : '))
if so > 2 : 
    is_nto = True
    for i in range(2, so ):
        if so % i == 0 : 
            break
        is_nto = False
else: 
    print(f'{so} không phải là số nguyên tố ')

if is_nto: 
    print(f'{so} không là số nguyên tố')
else: 
    print(f'{so} là số nguyen tố ')
