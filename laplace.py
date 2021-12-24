import random
from tkinter import *
from PIL import Image, ImageFilter, ImageTk
from matplotlib import pylab


def interface():
    root = Tk()
    root.geometry('{}x{}'.format(800, 630))

    header = Frame(root, width=800, height=50, bd=1, highlightbackground="black", highlightthickness=1.)
    header.pack_propagate(0)
    header.pack(side=TOP)

    header_label = Label(header, text="Drugi kolokvijum, zadatak br. 6",
                         font=("Arial", 20))
    header_label.pack(anchor=CENTER)

    # body = Frame(root, background='white', bd=1, width=800, height=600)
    body = Frame(root, background='white', bd=1, width=800, height=70)
    body.grid_propagate(0)
    # body.pack(side=TOP, expand=True)
    body.pack()

    x1label = Label(body, text="x1", font=("Arial", 16), padx=54, background='white')
    x1label.grid(row=1, column=1)
    x1 = Text(body, height=1, width=5, font=("Arial", 16))
    x1.grid(row=2, column=1)
    y1label = Label(body, text="y1", font=("Arial", 16), padx=54, background='white')
    y1label.grid(row=1, column=2)
    y1 = Text(body, height=1, width=5, font=("Arial", 16))
    y1.grid(row=2, column=2)

    x2label = Label(body, text="x2", font=("Arial", 16), padx=54, background='white')
    x2label.grid(row=1, column=3)
    x2 = Text(body, height=1, width=5, font=("Arial", 16))
    x2.grid(row=2, column=3)
    y2label = Label(body, text="y2", font=("Arial", 16), padx=54, background='white')
    y2label.grid(row=1, column=4)
    y2 = Text(body, height=1, width=5, font=("Arial", 16))
    y2.grid(row=2, column=4)

    x3label = Label(body, text="x3", font=("Arial", 16), padx=54, background='white')
    x3label.grid(row=1, column=5)
    x3 = Text(body, height=1, width=5, font=("Arial", 16))
    x3.grid(row=2, column=5)
    y3label = Label(body, text="y3", font=("Arial", 16), padx=54, background='white')
    y3label.grid(row=1, column=6)
    y3 = Text(body, height=1, width=5, font=("Arial", 16))
    y3.grid(row=2, column=6)

    def calculate_graph():
        x1val = int(x1.get(1.0, END).strip())
        x2val = int(x2.get(1.0, END).strip())
        x3val = int(x3.get(1.0, END).strip())
        y1val = int(y1.get(1.0, END).strip())
        y2val = int(y2.get(1.0, END).strip())
        y3val = int(y3.get(1.0, END).strip())
        y = [y1val, y2val, y3val]
        x = [x1val, x2val, x3val]
        print(x, y)

        minx = min(x)
        maxx = max(x)

        newy = []
        newx = [v * 0.1 for v in range(int(minx), int(maxx) * 10)]
        for x_value in newx:
            total = 0.0
            for index_tacke in range(3):
                temp = 1.0
                for index_tacke_2 in range(3):
                    if (index_tacke_2 != index_tacke):
                        temp = temp * (x_value - x[index_tacke_2]) / (x[index_tacke] - x[index_tacke_2])
                temp *= y[index_tacke]
                total += temp
            newy.append(total)

        total = 0.0
        # TODO: ne mora int, moze float na .10 razmaku
        # random_broj = random.randint(minx, maxx)
        random_broj = random.uniform(minx, maxx)
        for index_tacke in range(3):
            temp = 1.0
            for index_tacke_2 in range(3):
                if (index_tacke_2 != index_tacke):
                    temp = temp * (random_broj - x[index_tacke_2]) / (x[index_tacke] - x[index_tacke_2])
            temp *= y[index_tacke]
            total += temp

        lastx = x + newx
        lasty = y + newy
        lastx.sort()
        lasty.sort()

        pylab.plot(lastx, lasty)
        pylab.plot(random_broj, total, 'ro')
        pylab.show()

    # body2 = Frame(root, background='white', bd=1, width=800)
    body2 = Frame(root, background='white', bd=1, width=800, height=460)
    body2.pack_propagate(0)
    # body.pack(side=TOP, expand=True)
    body2.pack()

    btn = Button(body2, text="Plot Graph!", command=calculate_graph, font=("Arial", 16), pady=3, padx=3)
    btn.pack(pady=10)
    # btn.grid(row=3, column=3, pady=10)

    #
    # body3 = Frame(root, width=800)
    # body3.pack_propagate(0)
    # body3.pack(side=TOP)

    canvas = Canvas(body2, bd=0, relief=SUNKEN, width=220, height=189)
    elvis = Image.open("elvis.jpg")
    image = ImageTk.PhotoImage(elvis)

    canvas.create_image(0, 0, anchor=NW, image=image)
    canvas.pack(pady=(20, 5), side=LEFT)
    canvas2 = Canvas(body2, bd=0, relief=SUNKEN, width=220, height=189)

    canvas2.pack(pady=10, side=RIGHT)

    sb_num = StringVar()
    spinbox = Spinbox(body2, from_=-8, to=8, textvariable=sb_num, font=("Arial", 16))
    spinbox.pack(pady=5, side=BOTTOM)

    def convert_image():
        sb_num_int = int(sb_num.get())
        laplace_kernel = [(1 if sb_num_int < 0 else -1) for _ in range(abs(sb_num_int))]
        laplace_kernel += [0 for _ in range(8 - abs(sb_num_int))]
        laplace_kernel = laplace_kernel[:4] + [sb_num_int] + laplace_kernel[4:]

        img2 = elvis
        img2 = img2.convert("L")
        final2 = img2.filter(ImageFilter.Kernel((3, 3), tuple(laplace_kernel), 1, 0))
        final2.save("EinsteinLap.jpg")
        converted_image_action = ImageTk.PhotoImage(final2)
        print(converted_image_action)

        container = canvas2.create_image(0, 0, anchor=NW, image=converted_image_action)
        print(container)
        canvas2.itemconfig(container, image=final2)
        print(canvas2)

    btn = Button(body2, text="Laplace!", command=convert_image, font=("Arial", 16))
    btn.pack(pady=20, side=BOTTOM)

    footer = Frame(root, width=800, height=50, bd=1, highlightbackground="black", highlightthickness=1.)
    footer.pack_propagate(0)
    footer.pack(side=BOTTOM)

    footer_label = Label(footer, text="© 2021 Stefan Milicevic RIN-31/20 i Ljubisa Knezevic RIN-68/20",
                         font=("Arial", 17))
    footer_label.pack(anchor=CENTER)

    root.mainloop()


if __name__ == '__main__':
    interface()
