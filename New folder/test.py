from tkinter import *
from PIL import Image, ImageTk

# --- Timer function ---
def start_timer(new_win, duration):
    def count(sec):
        mins, secs = divmod(sec, 60)
        time_str = f"{mins:02d}:{secs:02d}"
        timer_label.config(text=time_str)
        if sec > 0:
            new_win.after(1000, count, sec-1)

    timer_label = Label(new_win, text="", font=("Comic Sans MS", 38, "bold"))
    timer_label.place(x=56,y=92)
    label4=Label(new_win,text="eggingggg....",font=("Comic Sans MS",12,"bold"),fg="dark grey")
    label4.place(x=70,y=44)
    count(duration)

# --- Function to open a new timer window ---
def open_timer(title, duration):
    new_win = Toplevel(root)
    new_win.title(title)
    new_win.geometry("250x260")
    new_win.resizable(False, False)
    start_timer(new_win, duration)
     


root = Tk()
root.title("Egg Timer")
root.geometry("400x450")  # window size

root.resizable(False, False)




start_img = Image.open("1.png").resize((160,120))
start_photo = ImageTk.PhotoImage(start_img)

stop_img = Image.open("2.png").resize((160,120))
stop_photo = ImageTk.PhotoImage(stop_img)

reset_img = Image.open("3.png").resize((160,120))
reset_photo = ImageTk.PhotoImage(reset_img)

exit_img = Image.open("4.png").resize((160,120))
exit_photo = ImageTk.PhotoImage(exit_img)

# Create 4 buttons
btn1 = Button(image=start_photo,bd=0, command=lambda: open_timer("Soft-Boiled Eggs", 5*60))
btn1.place(x=22,y=113)

btn2 = Button(image=stop_photo, bd=0,command=lambda: open_timer("Hard-Boiled Eggs", 10*60))
btn2.place(x=214,y=113)

btn3 = Button(image=reset_photo, bd=0,command=lambda: open_timer("Scrambled Eggs", 5*60))
btn3.place(x=22,y=279)

btn4 = Button(image=exit_photo, bd=0,command=lambda: open_timer("Poached Eggs", 3*60))
btn4.place(x=214,y=279)


label = Label(text="how do you want your eggs today?", font=("Arial", 13, "bold"), fg="black")
label.place(x=22,y=62)

label1 = Label(text="hard-boiled eggs", font=("Arial", 13, "bold"), fg="black")
label1.place(x=41, y=239)

label2 = Label(text="soft-boiled eggs", font=("Arial", 13, "bold"), fg="black")
label2.place(x=230, y=239)

label3 = Label(text="poached eggs", font=("Arial", 13, "bold"), fg="black")
label3.place(x=52, y=404)

label4 = Label(text="scrambled eggs", font=("Arial", 13, "bold"), fg="black")
label4.place(x=232, y=404)

root.mainloop()