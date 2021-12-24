from tkinter import *

import pylab


def main():
    points = int(input("Unesite broj ulaznih tacaka = "))
    x = []
    y = []
    print("Unesite koordinate ulaznih tacaka !");
    for i in range(points):
        x.append(float(input('x{:02d} = '.format(i))))
        y.append(float(input('y{:02d} = '.format(i))))
        print("------------>(x,y)=(", x[i], ",", y[i], ")")

    total = 0.0

    # Interpolacija :D

    minx = min(x)
    maxx = max(x)

    unet_broj = float(input("\nUnesite za koji x zelite interpolaciju f(x), x= "))

    while (unet_broj > maxx or unet_broj < minx):
        print("unesi i ne seri")
        unet_broj = float(input("\nUnesite za koji x zelite interpolaciju f(x), x= "))

    newy = []
    newx = [v * 0.1 for v in range(int(minx), int(maxx) * 10)]
    for x_value in newx:
        total = 0.0
        for index_tacke in range(points):
            temp = 1.0
            for index_tacke_2 in range(points):
                if (index_tacke_2 != index_tacke):
                    temp = temp * (x_value - x[index_tacke_2]) / (x[index_tacke] - x[index_tacke_2])
            temp *= y[index_tacke]
            total += temp
        newy.append(total)

    total = 0.0
    for index_tacke in range(points):
        temp = 1.0
        for index_tacke_2 in range(points):
            if (index_tacke_2 != index_tacke):
                temp = temp * (unet_broj - x[index_tacke_2]) / (x[index_tacke] - x[index_tacke_2])
        temp *= y[index_tacke]
        total += temp

    print('\nf(x) = f({}) = {}'.format(unet_broj, total))

    lastx = x + newx
    lasty = y + newy
    lastx.sort()
    lasty.sort()

    pylab.plot(lastx, lasty)
    pylab.plot(unet_broj, total, 'ro')
    pylab.show()


if __name__ == '__main__':
    main()
    root = Tk()
    root.mainloop()