import tkinter as tk
import tkinter.ttk as ttk

from comptrafficlight import CompTrafficLight

class CompTrafficLightApp:
    """ Graphical window that displays a traffic light and change button. """

    def __init__(self):
        root = tk.Tk()
        root.title("Traffic Light")
        frame = ttk.Frame(root)
        frame.pack()
        button = ttk.Button(frame, text='Change', command=self.do_button_press)
        self.light = CompTrafficLight(frame, 100, padding=25)
        button.grid(row=0, column=0)
        self.light.frame.grid(row=0, column=1)
        root.mainloop()               

    def do_button_press(self):
        """  The window manager calls this function when the user
             presses the graphical button. """
        self.light.change()

CompTrafficLightApp()