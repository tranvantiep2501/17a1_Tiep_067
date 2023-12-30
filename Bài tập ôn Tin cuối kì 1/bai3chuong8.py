a, b = map(int, input('Nhập 2 số a, b :').split())
if a == 0 and b != 0 :
    print('Phương trình vô nghiệm !')
elif a == 0 and b == 0 :
    print('Phương trình vô số nghiệm !')
elif a != 0 and b != 0 :
    print('Phương trình có nghiệm: ', 'x =', - b / a)
else:
    print('Vui lòng nhập lại')

# cách khác 
x, y = map(int, input('Nhập 2 số x, y :').split())
if a == 0 : 
    if b == 0 : 
        print('Phương trình có vô số nghiệm !')
    else: 
        print('Phương trình vô nghiệm !')
else:
    print('Phương trình có nghiệm a = ', - y / x)
    