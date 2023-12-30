x = int(input('SỐ tiền muốn đổi: '))
so_to_5 = x // 500000
so_du = x % 500000
print('Số tờ 500000 :', so_to_5)
so_to_2 = so_du // 200000
so_du = so_du % 200000
print('Số tờ 200000: ', so_to_2)
so_to_1 = so_du // 100000
so_du = so_du % 100000
print('Số tờ 100000 :', so_to_1)
so_to_50 = so_du // 50000
so_du = so_du % 50000
print('Số tờ 50000 :', so_to_50)
print('Tiền còn lại :', so_du)
# lưu ý: MUốn tìm số tờ thì dùng '//' là chia lấy phần nguyên, còn chia lấy phần dư là '%'
