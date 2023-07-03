import tkinter as tk
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from PIL import Image, ImageTk
from find_motion import find_motion
from identify import maincall

def capture():
    # Add your capture functionality here
    pass

def settings():
    # Add your settings functionality here
    pass

window = tk.Tk()
window.title("NextGen cctv")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('1080x700')

frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="NextGen cctv Camera")
label_font = font.Font(size=35, weight='bold', family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10, 10), column=2)

icon = Image.open('icons/spy.png')
icon = icon.resize((150, 150), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5, 10), column=2)

btn1_image = Image.open('icons/lamp.png')
btn1_image = btn1_image.resize((50, 50), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/rectangle-of-cutted-line-geometrical-shape.png')
btn2_image = btn2_image.resize((50, 50), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50, 50), Image.ANTIALIAS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn3_image = Image.open('icons/security-camera.png')
btn3_image = btn3_image.resize((50, 50), Image.ANTIALIAS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn6_image = Image.open('icons/incognito.png')
btn6_image = btn6_image.resize((50, 50), Image.ANTIALIAS)
btn6_image = ImageTk.PhotoImage(btn6_image)

btn4_image = Image.open('icons/recording.png')
btn4_image = btn4_image.resize((50, 50), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)

btn7_image = Image.open('icons/recording.png')
btn7_image = btn7_image.resize((50, 50), Image.ANTIALIAS)
btn7_image = ImageTk.PhotoImage(btn7_image)

btn8_image = Image.open('icons/camera.png')
btn8_image = btn8_image.resize((50, 50), Image.ANTIALIAS)
btn8_image = ImageTk.PhotoImage(btn8_image)

btn9_image = Image.open('icons/settings.png')
btn9_image = btn9_image.resize((50, 50), Image.ANTIALIAS)
btn9_image = ImageTk.PhotoImage(btn9_image)

# Button Styling
btn_font = font.Font(size=25)
# Button Styling
btn_font = font.Font(size=25)
button_config = {
    'height': 90,
    'width': 180,
    'compound': 'left',
    'font': btn_font,
    'bd': 4,
    'highlightthickness': 0,
    'bg': '#f0f0f0',  # Button background color
    'fg': 'green',  # Button text color
    'activebackground': '#dddddd',  # Button background color when clicked
    'activeforeground': 'black',  # Button text color when clicked
}

# Buttons
btn1 = tk.Button(frame1, text='Monitor', command=find_motion, image=btn1_image, **button_config)
btn1.grid(row=3, pady=(20, 10))

btn2 = tk.Button(frame1, text='Rectangle', command=rect_noise, image=btn2_image, **button_config)
btn2.grid(row=3, pady=(20, 10), column=3, padx=(20, 5))

btn3 = tk.Button(frame1, text='Noise', command=noise, image=btn3_image, **button_config)
btn3.grid(row=5, pady=(20, 10))

btn4 = tk.Button(frame1, text='Record', command=record, image=btn4_image, **button_config)
btn4.grid(row=5, pady=(20, 10), column=3)

btn5 = tk.Button(frame1, command=window.quit, image=btn5_image, **button_config)
btn5.grid(row=6, pady=(20, 10), column=2)

btn6 = tk.Button(frame1, text='In Out', command=in_out, image=btn6_image, **button_config)
btn6.grid(row=5, pady=(20, 10), column=2)

btn7 = tk.Button(frame1, text='Identify', command=maincall, image=btn7_image, **button_config)
btn7.grid(row=3, column=2, pady=(20, 10))

btn8 = tk.Button(frame1, text='Capture', command=capture, image=btn8_image, **button_config)
btn8.grid(row=7, pady=(20, 10))

btn9 = tk.Button(frame1, text='Settings', command=settings, image=btn9_image, **button_config)
btn9.grid(row=7, column=2, pady=(20, 10))

frame1.pack()
window.mainloop()
