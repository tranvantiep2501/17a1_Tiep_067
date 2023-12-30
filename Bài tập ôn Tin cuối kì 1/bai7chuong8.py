so_kwh = int(input('Nhập số Kwh tiêu thụ : '))
if so_kwh > 0 and so_kwh <= 50 : 
    sotien = so_kwh * 1.678 
    print('Số tiền điện là : ', sotien)
elif so_kwh > 50 and so_kwh <= 100 : 
    sotien = 50 * 1.678 + (so_kwh - 50) * 1.734
    print('Số tiền điện là : ', sotien)
elif so_kwh > 100 and so_kwh <= 200 : 
    sotien = 50 * 1.678 + 100 * 1.734 + (so_kwh - 100) * 2.014
    print('Số tiền điện là : ', sotien)
elif so_kwh > 200 and so_kwh <= 300 : 
    sotien = 50 * 1.678 + 100 * 1.734 + 200 * 2.014 + (so_kwh - 200) * 2.536
    print('Số tiền điện là : ', sotien)
elif so_kwh > 300 and so_kwh <= 400 : 
    sotien = 50 * 1.678 + 100 * 1.734 + 200 * 2.014 + 300 * 2.536 + (so_kwh - 300) * 2.834
    print('Số tiền điện là : ', sotien)
elif so_kwh > 400 : 
    sotien = 50 * 1.678 + 100 * 1.734 + 200 * 2.014 + 300 * 2.536 + 400 * 2.834 + (so_kwh - 400) * 2.927
    print('Số tiền điện là : ', sotien)
else: 
    print('TÔi ĐÃ NỢ BẠN HEHHEHEE')
    