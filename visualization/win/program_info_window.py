from tkinter import *


def download():
    window = Tk()
    window.title("О программе")
    window.resizable(FALSE, FALSE)

    Label(window, text="В разработке...").pack()

    window.mainloop()


if __name__ == "__main__":
    download()
