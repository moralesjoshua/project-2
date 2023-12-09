from guiProject2 import *


def main():
    window = Tk()
    window.title('Calculator')
    window.geometry('500x400')
    window.resizable(False, False)
    Calculator(window)
    window.mainloop()


if __name__ == "__main__":
    main()
