"""BMI Calc V1.1 by Steve Shambles. (c) March 2023. Freeware, MIT Licence

V1.1:Changed Meters to centimeters and rechecked all calculations,
     Code tidy up,
     made bg powderblue (changable. bg_theme = 'powderblue'.
     resized logo to fit width properly now called bmi2.jpg
"""

import tkinter as tk
import tkinter.messagebox
import sys
from PIL import Image, ImageTk


def show_ratings():
    """ Show Body Mass Index scales in a pop up box. """
    tk.messagebox.showinfo('BMI Limits',
                           'A BMI below 18.5 is considered underweight.\n\n'
                           'A BMI between 18.5 and 24.9 is considered healthy\n\n'
                           'A BMI between 25 and 29.9 is considered overweight.\n\n'
                           'A BMI of between 30 and 39.9 is considered obese.\n\n'
                           'A BMI of between 40 + is considered severe obesity.\n\n'
                           '\nSource: NHS England.\nPlease see notes in info menu.')

def calculate_bmi():
    """ Calculate the BMI using weight and height user inputs. """
    try:
        if weight_unit.get() == 'Kgrams':
            weight = float(weight_entry.get())
        elif weight_unit.get() == 'Pounds':
            weight = float(weight_entry.get()) / 2.20462
        elif weight_unit.get() == 'Stones':
            weight = float(weight_entry.get()) * 14 / 2.20462
    except ValueError as e:
        return

    try:
        if height_unit.get() == 'Inches':
            height = float(height_entry.get()) * 2.54
        elif height_unit.get() == 'Centimeters':
            height = float(height_entry.get())
    except ValueError as e:
        return

    bmi = weight / ((height/100) ** 2)
    msg = ''

    if int(bmi) < 18.5:
        msg = 'Underweight'

    if int(bmi) >= 18.5 and int(bmi) <= 24.9:
        msg = 'Healthy'

    if int(bmi) > 24.9 and int(bmi) <= 29.9:
        msg = 'Overweight'

    if int(bmi) > 29.9 and int(bmi) <= 39.9:
        msg = 'Obese'

    if int(bmi) >= 40:
        msg = 'Severely Obese'

    msg = msg + '\n\nPlease see important notes in info menu.'

    bmi_result = f'\nYour BMI is: {bmi:.2f}\n\n' + str(msg)
    tk.messagebox.showinfo('BMI Calc result:', bmi_result)



def about():
    """ Basic info and how to use prg in a pop up."""
    tk.messagebox.showinfo('BMI Calc help',
                           '\nInput your weight and'
                           ' choose your preferred\n'
                           'option of kilograms, pounds or stones.\n\n'
                           'Next enter your height in inches or centimeters.\n'
                           '\nNow click on Calculate to reveal your BMI.\n'
                           '\nThis program is FREEWARE,\nbut remains (c) Steve Shambles Feb 2023')


def notes():
    """ Important notes about problems with BMI for certain body types. """
    tk.messagebox.showinfo('BMI Calc important notes',
                           'It is important to note that while BMI can be '
                           'a useful tool for\n'
                           'assessing weight status, it is not a perfect '
                           'measure.\n\nFor example,\n'
                           'it does not take into account factors like '
                           'muscle mass or\n'
                           'body composition, which can affect a persons '
                           'weight but not\n'
                           'necessarily indicate poor health.\n\n'
                           'Additionally, some people may fall into the '
                           'healthy range but still\n'
                           'have excess body fat, while others may have a '
                           'high BMI but be\n'
                           'very physically fit.\n\nTherefore, '
                           'it is always best to consult with a\n'
                           'healthcare professional to determine what a '
                           'healthy weight range is\n'
                           'for you, based on your individual health and '
                           'lifestyle factors.')


root = tk.Tk()
root.title('BMI Calc V1.1')
root.resizable(False, False)
bg_theme = 'powderblue'
root.config(bg=bg_theme)

logo_frame = tk.LabelFrame(root)
logo_frame.grid()

# Display logo in logo frame.
try:
    logo_image = Image.open('bmi2.jpg')
except FileNotFoundError as e:
    tk.messagebox.showinfo('FileNotFoundError',
                           'bmi2.jpg not found.')
    root.destroy()
    sys.exit(1)

logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(logo_frame, image=logo_photo)
logo_label.logo_image = logo_photo
logo_label.grid(row=0, column=0)

weight_label = tk.Label(root, fg='blue',bg=bg_theme,
                        font='helvetica 10 bold',
                        text='Input your weight')
weight_label.grid(pady=(10, (0)))

weight_entry = tk.Entry(root)
weight_entry.grid(padx=8)

weight_frame = tk.Frame(root)
weight_frame.grid(padx=10, pady=10)

weight_unit = tk.StringVar(value='Stones')

kg_button = tk.Radiobutton(weight_frame, bg=bg_theme, text='Kgrams',
                           variable=weight_unit, value='Kgrams')
kg_button.grid(row=2, column=0)

lb_button = tk.Radiobutton(weight_frame,bg=bg_theme, text='Pounds',
                           variable=weight_unit, value='Pounds')
lb_button.grid(row=2, column=1)

st_button = tk.Radiobutton(weight_frame, bg=bg_theme, text='Stones',
                           variable=weight_unit, value='Stones')
st_button.grid(row=2, column=2)

height_label = tk.Label(root, fg='blue', bg=bg_theme,
                        font='helvetica 10 bold',
                        text='Input your height')
height_label.grid(pady=(10, (0)))

height_entry = tk.Entry(root)
height_entry.grid()

height_frame = tk.Frame(root)
height_frame.grid(padx=10, pady=5)

height_unit = tk.StringVar(value='Inches')

in_button = tk.Radiobutton(height_frame, bg=bg_theme, text='Inches',
                           variable=height_unit, value='Inches')
in_button.grid(row=7, column=0)
m_button = tk.Radiobutton(height_frame, bg=bg_theme, text='Centimeters',
                          variable=height_unit, value='Centimeters')
m_button.grid(row=7, column=1)

calculate_button = tk.Button(root, font='helvetica 12 bold',
                             text='Calculate',
                             bg='lime', command=calculate_bmi)
calculate_button.grid(pady=(10, (20)))


# Create drop down menu.
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Info', menu=file_menu)
file_menu.add_command(label='BMI ratings', command=show_ratings)
file_menu.add_command(label='Notes', command=notes)
file_menu.add_command(label='Help', command=about)
root.config(menu=menu_bar)


root.mainloop()
