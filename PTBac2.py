import math

a = float(input('Nhập a:'))
b = float(input('Nhập b:'))
c = float(input('Nhập c:'))


def  giaiPT(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print('PT có vô số nghiêm!')
                return
            else:
                print('Phương trình vô nghiêm!')
                return
        else:
            print('Phương trình có nghiêm x=', -c / b)
    else:
        if (a + b + c) == 0:
            print('Phương trình có nghiêm x1=', 1)
            print('Phương tình có nghiệm x2=', c / a)
            return
        if (a - b + c) == 0:
            print('Phương trình có nghiệm x1=', -1)
            print('Phương trình có nghiệm x2=', -c / a)
            return
        denta = b * b - 4 * a * c
        if denta < 0:
            print('Phương trình vô nghiệm!')
        elif denta == 0:
            print('Phương trình có nghiệm x1=x2=', -b / 2 * a)
        elif denta > 0:
            x1 = (-b + math.sqrt(denta)) / (2 * a)
            x2 = (-b - math.sqrt(denta)) / (2 * a)
            print('Phương trình có nghiêm x1=', x1)
            print('Phương trình có nghiêm x2=', x2)


print(giaiPT(a, b, c))
