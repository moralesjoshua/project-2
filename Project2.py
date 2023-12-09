from guiProject2 import *


def main():
    window = Tk()
    window.title('Calculator')
    window.geometry('300x420')
    window.resizable(False, False)
    Calculator(window)
    window.mainloop()


if __name__ == "__main__":
    main()
