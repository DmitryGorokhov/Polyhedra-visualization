from tkinter import *
import manager
from win import authors_info_window as aiw, program_info_window as piw
import settings


def draw(option):
    manager.draw(option)


def show_info_about_program():
    piw.download()


def show_info_about_authors():
    aiw.download()


def main():
    window = Tk()
    window.title("EXAMPLE")
    window.resizable(FALSE, FALSE)

    selected = IntVar()
    selected.set("0")

    """ SECTIONS """
    opt_frame = Frame(window)
    opt_frame.pack(anchor=W)

    btn_frame = Frame(window, pady=15)
    btn_frame.pack()

    authors_frame = Frame(window, pady=5)
    authors_frame.pack(anchor=W)

    """ OPTIONS SECTION """

    Label(opt_frame, text="Выберите вариант визуализации", font="Ariel, 18", pady=15).pack()

    for text, value in settings.OPTIONS:
        Radiobutton(opt_frame, text=text, value=value,
                    variable=selected, font="Ariel, 16").pack(anchor=W)

    """ BUTTONS SECTION """

    Button(btn_frame, text="Показать", font="Ariel, 18",
           width=24, bg="pale green4",
           command=lambda: draw(selected.get())).grid(row=0, column=0)

    Button(btn_frame, text="О программе", font="Ariel, 18",
           bg="azure3",
           command=show_info_about_program).grid(row=0, column=1)

    Button(btn_frame, text="Об авторах", font="Ariel, 18",
           bg="medium orchid",
           command=show_info_about_authors).grid(row=0, column=2)

    """ AUTHORS SECTION """

    i = 0
    for role, info in settings.AUTHORS:
        Label(authors_frame, text=role+":", font="Ariel, 14").grid(row=i, column=0, sticky=W)
        Label(authors_frame, text=info, font="Ariel, 14").grid(row=i, column=1, sticky=W)
        i += 1

    window.mainloop()


if __name__ == "__main__":
    main()
