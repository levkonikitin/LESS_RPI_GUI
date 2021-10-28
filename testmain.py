# Import the required libraries
from tkinter import *
from PIL import ImageTk, Image

# env variables
window_size = "1024x600"
header_sizex, header_sizey = 1024, 114
 
# Create an instance of tkinter frame
win = Tk()
win.title("Substation Technical Training Simulator")

# Set the geometry of frame
win.geometry("1024x600")

# Create a frame
header = Frame(win, width=1024, height=114).place(x=0, y=0)
footer = Frame(win, width=1024, height=64).place(x=0, y=536)
body = Frame(win, width=1024, height=422).place(x=0, y=100)


def draw_header():
    global logo_img
    logo_img = ImageTk.PhotoImage(Image.open('logo.png'))
    global UI_image
    UI_image = ImageTk.PhotoImage(Image.open('./UI/Rectangle 7.png'))

    Label(header, image=logo_img).place(x=0, y=14)
    Label(header, image=UI_image, text="Substation Technical \n Training Simulator", font=('graphik', 30, 'bold'),
          foreground="white", compound="center").place(x=512, y=14)


# a function that clears everything of the page, make sure to only define one window and frame
def clear_body_frame():
    for widgets in win.winfo_children():
        widgets.destroy()


def main_page():
    clear_body_frame()
    draw_header()
    main_name = Label(body, text='main page', font=('nunito', 28), background='grey', foreground='black').pack(pady=20, side="bottom")
    to_settings_page = Button(body, text='settings', command=settings_page).place(x=600, y=200)


def settings_page():
    clear_body_frame()
    draw_header()
    settings_name = Label(body, text='settings page', font=('nunito', 28), background='grey', foreground='black').pack()
    to_main_page = Button(body, text='main menu', command=main_page).pack(pady=20)


main_page()

win.mainloop()
