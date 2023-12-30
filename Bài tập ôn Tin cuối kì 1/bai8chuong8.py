phong = int(input('Xin mời quý khách nhập số phòng !\n'))
dem = int(input('Xin mời quý khách nhập số đêm !\n'))
if dem == 1 : 
        if phong == 1 : 
            print('Số tiền cho phòng Standard trong 1 đêm là : ', 1260000, 'vnđ') 
        elif phong == 2 : 
            print('Số tiền cho phòng Superior Garden View trong 1 đêm là : ', 1550000, 'vnđ')
        elif phong == 3 : 
            print('Số tiền cho phòng Superior Ocean View trong 1 đêm là : ', 1830000, 'vnđ')
        elif phong == 4 : 
            print('Số tiền cho phòng Garden View Bungalow trong 1 đêm là : ', 1830000, 'vnđ') 
        elif phong == 5 : 
            print('Số tiền cho phòng Pool VIew Bungalow trong 1 đêm là : ', 2120000, 'vnđ') 
        elif phong == 6 : 
            print('Số tiền cho phòng Family Room trong 1 đêm là : ', 2120000, 'vnđ') 
        elif phong == 7 : 
            print('Số tiền cho phòng Beach Front Bungalow trong 1 đêm là : ', 2540000, 'vnđ')  
        elif phong == 8 : 
            print('Số tiền cho phòng VIP sea View trong 1 đêm là : ', 4800000, 'vnđ') 
        else: 
            print('Vui lòng nhập lại số phòng')
elif dem == 2 or dem == 3 : 
        print('Bạn đã được giảm 25% giá tiền khi ở từ 2 đến 3 đêm so với số tiền ở 1 đêm !!')
        if phong == 1 : 
            print('Số tiền cho phòng Standard trong 2-3 đêm là : ', dem * (1260000 - (25 / 100 * 1260000)), 'vnđ') 
        elif phong == 2 : 
            print('Số tiền cho phòng Superior Garden View trong 2-3 đêm là : ', dem * (1550000 - (25 / 100 * 1550000)), 'vnđ')
        elif phong == 3 : 
            print('Số tiền cho phòng Superior Ocean View trong 2-3 đêm là : ', dem * (1830000 - (25 / 100 * 1830000)), 'vnđ')
        elif phong == 4 : 
            print('Số tiền cho phòng Garden View Bungalow trong 2-3 đêm là : ', dem * (1830000 - (25 / 100 * 1830000)), 'vnđ') 
        elif phong == 5 : 
            print('Số tiền cho phòng Pool VIew Bungalow trong 2-3 đêm là : ', dem * (2120000 - (25 / 100 * 2120000)), 'vnđ') 
        elif phong == 6 : 
            print('Số tiền cho phòng Family Room trong 2-3 đêm là : ', dem * (2120000 - (25 / 100 * 2120000)), 'vnđ') 
        elif phong == 7 : 
            print('Số tiền cho phòng Beach Front Bungalow trong 2-3 đêm là : ', dem * (2540000 - (25 / 100 * 2540000)), 'vnđ')  
        elif phong == 8 : 
            print('Số tiền cho phòng VIP sea View trong 2-3 đêm là : ', dem * (4800000 - (25 / 100 * 4800000)), 'vnđ') 
        else: 
            print('Vui lòng nhập lại số phòng')
elif dem >= 4 : 
        print('Bạn đã được giảm 30% giá tiền khi ở từ 4 đêm so với số tiền ở 1 đêm !!')
        if phong == 1 : 
            print('Số tiền cho phòng Standard từ 4 đêm là : ', dem * (1260000 - (30 / 100 * 1260000)), 'vnđ') 
        elif phong == 2 : 
            print('Số tiền cho phòng Superior Garden View từ 4 đêm là : ', dem * (1550000 - (30 / 100 * 1550000)), 'vnđ')
        elif phong == 3 : 
            print('Số tiền cho phòng Superior Ocean View từ 4 đêm là : ', dem * (1830000 - (30 / 100 * 1830000)), 'vnđ')
        elif phong == 4 : 
            print('Số tiền cho phòng Garden View Bungalow từ 4 đêm là : ', dem * (1830000 - (30 / 100 * 1830000)), 'vnđ') 
        elif phong == 5 : 
            print('Số tiền cho phòng Pool VIew Bungalow từ 4 đêm là : ', dem * (2120000 - (30 / 100 * 2120000)), 'vnđ') 
        elif phong == 6 : 
            print('Số tiền cho phòng Family Room từ 4 đêm là : ', dem * (2120000 - (30 / 100 * 2120000)), 'vnđ') 
        elif phong == 7 : 
            print('Số tiền cho phòng Beach Front Bungalow từ 4 đêm là : ', dem * (2540000 - (30 / 100 * 2540000)), 'vnđ')  
        elif phong == 8 : 
            print('Số tiền cho phòng VIP sea View từ 4 đêm là : ', dem * (4800000 - (30 / 100 * 4800000)), 'vnđ') 
        else: 
            print('Vui lòng nhập lại số phòng')
else: 
    print('Bạn có ở không ???? ')