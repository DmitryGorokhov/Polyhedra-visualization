from tkinter import *
import manager
import program_info_window as piw
import settings


def draw(option):
    manager.draw(option)


def show_info():
    piw.download()


def main():
    window = Tk()
    window.title("Разбиение сферы на равные участки")
    window.resizable(FALSE, FALSE)

    selected = IntVar()
    selected.set("0")

    """ Structure """
    opt_frame = Frame(window)
    opt_frame.pack(anchor=W)

    btn_frame = Frame(window, pady=8)
    btn_frame.pack()

    """ Options """

    Label(opt_frame, text="Выберите вариант визуализации", font="Ariel, 16", pady=15).pack()

    for text, value in settings.OPTIONS:
        Radiobutton(opt_frame, text=text, value=value,
                    variable=selected, font="Ariel, 14").pack(anchor=W)

    """ Buttons """

    Button(btn_frame, text="Показать", font="Ariel, 14",
           width=24, bg="pale green4",
           command=lambda: draw(selected.get())).grid(row=0, column=0)

    Button(btn_frame, text="О программе", font="Ariel, 14",
           bg="light grey",
           command=show_info).grid(row=0, column=1)

    window.mainloop()


if __name__ == "__main__":
    main()
