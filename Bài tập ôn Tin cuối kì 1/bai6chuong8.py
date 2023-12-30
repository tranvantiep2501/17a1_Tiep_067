loai_xe = int(input('Nhập loại xe bạn muốn đi : '))
so_km = float(input('Đi bao nhiêu kilomet : '))
tgian_cho = float(input('Thời gian chờ : '))
if tgian_cho <= 5 : 
    print('Không tính tiền chờ')
else:
    print('Tiền chờ là : ', 800 * (tgian_cho - 5), 'vnđ')
if loai_xe == 4 : 
    if so_km <= 0.8 : 
        tiencho = so_km * 11000
        print('Tiền di chuyển là :', tiencho, 'vnđ')
    elif so_km > 0.8 and so_km <= 20 :
        tiencho = so_km * 12100
        print('Tiền di chuyển là : ', tiencho, 'vnđ')
    else: 
        tiencho = so_km * 10000
        print('Tiền di chuyển là :', tiencho, 'vnđ')
    print('Tiền cước là : ', (800 * (tgian_cho - 5)) + tiencho, 'vnđ')
elif loai_xe == 7 : 
    if so_km <= 0.8 : 
        tiencho = so_km * 13000
        print('Tiền di chuyển là :', tiencho, 'vnđ')
    elif so_km > 0.8 and so_km <= 30:
        tiencho = so_km * 14100
        print('Tiền di chuyển là : ', tiencho, 'vnđ')
    else: 
        tiencho = so_km * 12000
        print('Tiền di chuyển là :', tiencho, 'vnđ')
    print('Tiền cước là : ', (800 * (tgian_cho - 5)) + tiencho, 'vnđ')
else: 
    print('KHông có xe !!! ô kê')