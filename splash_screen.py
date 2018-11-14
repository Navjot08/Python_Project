import tkinter as tk
import time

# root = tk.Tk()
from login_page import Login


class Splash(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Splash")
        self.geometry("1280x720")

        image_file = "quiz.gif"

        image = tk.PhotoImage(file=image_file)

        lbl = tk.Label(self,image=image, height=720, width=1280)
        lbl.pack()

        ## required to make window show before the program gets to the mainloop
        self.update()
        time.sleep(2)


        ## finished loading so destroy splash
        self.destroy()
        logg = Login()
        ## show window again
      #  self.deiconify()


if __name__ == "__main__":
    spl = Splash()
    spl.mainloop()
