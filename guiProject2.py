from tkinter import *
import math


class Calculator:
    """
    Initializes the class
    """
    def __init__(self, window):
        self.window = window

        self.equation_text = ""
        self.equation_label = StringVar()

        self.label = Label(window, textvariable=self.equation_label, width=24, height=2)
        self.label.pack()

        self.frame = Frame(self.window)
        self.frame.pack()

        self.button7 = Button(self.frame, text=7, height=4, width=4, font=35, command=lambda: self.button_press(7))
        self.button7.grid(row=1, column=0)

        self.button8 = Button(self.frame, text=8, height=4, width=4, font=35, command=lambda: self.button_press(8))
        self.button8.grid(row=1, column=1)

        self.button9 = Button(self.frame, text=9, height=4, width=4, font=35, command=lambda: self.button_press(9))
        self.button9.grid(row=1, column=2)

        self.button4 = Button(self.frame, text=4, height=4, width=4, font=35, command=lambda: self.button_press(4))
        self.button4.grid(row=2, column=0)

        self.button5 = Button(self.frame, text=5, height=4, width=4, font=35, command=lambda: self.button_press(5))
        self.button5.grid(row=2, column=1)

        self.button6 = Button(self.frame, text=6, height=4, width=4, font=35, command=lambda: self.button_press(6))
        self.button6.grid(row=2, column=2)

        self.button1 = Button(self.frame, text=1, height=4, width=4, font=35, command=lambda: self.button_press(1))
        self.button1.grid(row=3, column=0)

        self.button2 = Button(self.frame, text=2, height=4, width=4, font=35, command=lambda: self.button_press(2))
        self.button2.grid(row=3, column=1)

        self.button3 = Button(self.frame, text=3, height=4, width=4, font=35, command=lambda: self.button_press(3))
        self.button3.grid(row=3, column=2)

        self.button0 = Button(self.frame, text=0, height=4, width=4, font=35, command=lambda: self.button_press(0))
        self.button0.grid(row=4, column=0)

        self.plus_button = Button(self.frame, text='+', height=4, width=4, font=35, command=lambda: self.button_press('+'))
        self.plus_button.grid(row=1, column=3)

        self.minus_button = Button(self.frame, text='-', height=4, width=4, font=35, command=lambda: self.button_press('-'))
        self.minus_button.grid(row=2, column=3)

        self.multiply_button = Button(self.frame, text='*', height=4, width=4, font=35, command=lambda: self.button_press('*'))
        self.multiply_button.grid(row=3, column=3)

        self.divide_button = Button(self.frame, text='/', height=4, width=4, font=35, command=lambda: self.button_press('/'))
        self.divide_button.grid(row=4, column=3)

        self.equal_button = Button(self.frame, text='=', height=4, width=4, font=35, command=self.equal)
        self.equal_button.grid(row=4, column=2)

        self.decimal_button = Button(self.frame, text='.', height=4, width=4, font=35, command=lambda: self.button_press('.'))
        self.decimal_button.grid(row=4, column=1)

        self.clear_button = Button(self.frame, text='CLEAR', height=3, width=4, font=35, command=self.clear)
        self.clear_button.grid(row=0, column=0)

        self.exponent_button = Button(self.frame, text='^', height=3, width=4, font=35, command=lambda: self.button_press('**'))
        self.exponent_button.grid(row=0, column=2)

        self.modulus_button = Button(self.frame, text='%', height=3, width=4, font=35, command=lambda: self.button_press('%'))
        self.modulus_button.grid(row=0, column=3)

        self.square_root_button = Button(self.frame, text='√', height=3, width=4, font=35, command=self.square_root)
        self.square_root_button.grid(row=0, column=1)

    def button_press(self, num: [int, float, str]) -> None:
        """
        Deals with the button pressed along with its associated value

        Parameters: The number or operator that was pressed.
        """
        self.equation_text = self.equation_text + str(num)
        self.equation_label.set(self.equation_text)

    def equal(self):
        """
        Evaluates the equation then updates the equation label
        """
        try:
            total = str(eval(self.equation_text))
            self.equation_label.set(total)
            self.equation_text = total
        except SyntaxError:
            self.equation_label.set("Syntax Error")
            self.equation_text = ""
        except ZeroDivisionError:
            self.equation_label.set("Zero Error")
            self.equation_text = ""

    def clear(self):
        """
        Clears the label
        """
        self.equation_label.set("")
        self.equation_text = ""

    def square_root(self):
        """
        Evaluates square root in float
        """
        try:
            result = math.sqrt(float(self.equation_text))
            self.equation_label.set(result)
            self.equation_text = str(result)
        except ValueError:
            self.equation_label.set("Error")
            self.equation_text = ""
