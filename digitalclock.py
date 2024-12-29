import tkinter as tk 
import time

window = tk.Tk()
window.geometry("300x300")
window.title("Digital Clock")

blank = tk.Label(window, font = ("arial",30,"bold"))
blank.pack(anchor = "center" )

def clocks():
  clock = time.strftime("%I:%M:%S %p %Z")
  blank.config(text=clock )
  blank.after(1000,clocks)

clocks()









window.mainloop()
