from tkinter import *


def download():
    window = Tk()
    window.title("О программе")
    window.resizable(FALSE, FALSE)

    with open("AboutMe.txt") as f:
        Label(window, text=f.readline(), font="Ariel, 16").pack()
        text = Text(window, width="57", height="15", font="Ariel, 14")
        content = f.readline()
        while content:
            text.insert(INSERT, content)
            content = f.readline()
        text.configure(state='disabled')
        text.pack(anchor=W)

    Label(window, text="2020 год", font="Ariel, 12", pady=4).pack()
    window.mainloop()


if __name__ == "__main__":
    download()
