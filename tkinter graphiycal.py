from tkinter import *
wind = Tk()
wind.title("name of window")
wind.geometry("300x300+200+200") # direction

icon = PhotoImage(file='image.png') # icon image change
wind.iconphoto(True, icon)          # icon image change

screen_w = wind.winfo_screenwidth() # width of monitor
screen_h = wind.winfo_screenheight() # height of monitor

print(f"show{screen_h, screen_w}") # print monitor 

# wind.quit()

wind.mainloop()
