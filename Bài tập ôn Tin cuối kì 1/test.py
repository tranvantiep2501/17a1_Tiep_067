
import csv
# Tính thuế
def tinh_thue(doanh_thu):
    if doanh_thu > 5000000:
        return doanh_thu * 0.1
    else:
        return doanh_thu * 0.05
# Tạo cửa hàng mới
def tao_cua_hang():
    ma_cua_hang = input("Nhập mã của hàng : ")
    ten_cua_hang = input("Nhập tên cửa hàng : ")
    von_dau_tu = float(input("Nhập vốn đầu tư: "))
    doanh_thu = float(input("Nhập doanh thu cửa hàng: "))
    thue = tinh_thue(doanh_thu)
    loi_nhuan = doanh_thu - thue

    return [ma_cua_hang, ten_cua_hang, von_dau_tu, doanh_thu, thue, loi_nhuan]
# Mở fiel csv
def mo_file():
    try:
        with open('files/ds_cua_hang.csv', mode='r',encoding='utf-8') as file:
            print("Đã Mở file {ds_cua_hang.csv}")
            reader = csv.reader(file)
            return [row for row in reader ]
    except FileNotFoundError:
        return []
# Lưu file
def luu_file(ds_cua_hang):
    with open('files/ds_cua_hang.csv', mode='w', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(ds_cua_hang)
# in danh sách cửa hàng 
def in_danh_sach(ds_cua_hang):
    print("Danh sách cửa hàng :")
    for cua_hang in ds_cua_hang:
        print(cua_hang)
# xawpsseep theo doanh thu 
def sap_xep_theo_doanh_thu(ds_cua_hang):
    ds_cua_hang.sort(key=lambda x: x.doanh_thu, reverse=True)

# Menu lựa chọn 
def main():
    ds_cua_hang = mo_file()

    while True:
        print("-----MENU------")
        print("1.Mở file ")
        print("2.Nhập thông tin cửa hàng mới(Tự động tính thuế)")
        print("3.In Thông tin cửa hàng ")
        print("4.xắp xếp theo tăng dần  ")
        print("5.Thoát ")
        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == '1':
            mo_file()
        elif lua_chon == '2':
            cua_hang_moi = tao_cua_hang()
            ds_cua_hang.append(cua_hang_moi)
            luu_file(ds_cua_hang)
            print("Lưu thông tin thành công!")
        elif lua_chon == '3':
            in_danh_sach(ds_cua_hang)
        elif lua_chon == '4':
            sap_xep_theo_doanh_thu(ds_cua_hang)
        elif lua_chon =='5':
            break
        else:
            print("Lựa chọn không hợp lệ mời chọn lại ")

    main()