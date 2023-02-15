import tkinter as tk
import tkinter.messagebox


def show_ratings():
    tk.messagebox.showinfo('BMI Limits',
                           'A BMI below 18.5 is considered underweight.\n\n'
                           'A BMI between 18.5 and 24.9 is considered healthy\n\n'
                           'A BMI between 25 and 29.9 is considered overweight.\n\n'
                           'A BMI of between 30 and 39.9 is considered obese.\n\n'
                           'A BMI of between 40 + is considered severe obesity.\n\n'
                           '\nSource: NHS England.\nPlease see notes in info menu.')


def calculate_bmi():
    if not weight_entry.get():
        return

    if weight_unit.get() == "kg":
        weight = float(weight_entry.get())
    elif weight_unit.get() == "lb":
        weight = float(weight_entry.get()) / 2.20462
    elif weight_unit.get() == "st":
        weight = float(weight_entry.get()) * 14 / 2.20462

    if not height_entry.get():
        return

    if height_unit.get() == "m":
        height = float(height_entry.get())
    elif height_unit.get() == "in":
        height = float(height_entry.get()) * 0.0254

    bmi = weight / (height ** 2)
    msg = ""

    if int(bmi) < 18.5:
        msg = "Underweight"

    if int(bmi) >= 18.5 and int(bmi) <= 24.9:
        msg = "Healthy"

    if int(bmi) > 24.9 and int(bmi) <= 29.9:
        msg = "Overweight"

    if int(bmi) > 29.9 and int(bmi) <= 39.9:
        msg = "Obese"

    if int(bmi) >= 40:
        msg = "Severely Obese"

    bmi_label.config(font="helvetica 11",
                     text=f"\nYour BMI is: {bmi:.2f}\n" + str(msg))


def reset():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    bmi_label.config(text="")


def about():
    tk.messagebox.showinfo('BMI Calc help V0.16',
                           '\nInput your weight and'
                           ' choose your preferred\n'
                           'option of kilograms, pounds or stones.\n\n'
                           'Next enter your height in inches or meters.\n'
                           '\nNow click on Calculate to reveal your BMI.\n'
                           '\nThis program is FREEWARE,\nbut remains (c) Steve Shambles Feb 2023')


def notes():
    tk.messagebox.showinfo('BMI Calc important notes',
                           'It is important to note that while BMI can be a useful tool for\n'
                           'assessing weight status, it is not a perfect measure.\n\nFor example,\n'
                           'it does not take into account factors like muscle mass or\n'
                           'body composition, which can affect a persons weight but not\n'
                           'necessarily indicate poor health.\n\n'
                           'Additionally, some people may fall into the healthy range but still\n'
                           'have excess body fat, while others may have a high BMI but be\n'
                           'very physically fit.\n\nTherefore, it is always best to consult with a\n'
                           'healthcare professional to determine what a healthy weight range is\n'
                           'for you, based on your individual health and lifestyle factors.')


root = tk.Tk()
root.title("BMI Calc V0.16")

weight_label = tk.Label(root, text="Input your weight")
weight_label.grid()

weight_entry = tk.Entry(root)
weight_entry.grid(padx=8)

weight_frame = tk.Frame(root)
weight_frame.grid(padx=10, pady=10)

weight_unit = tk.StringVar(value="st")
kg_button = tk.Radiobutton(weight_frame, text="kg",
                           variable=weight_unit, value="kg")
kg_button.grid(row=2, column=0)

lb_button = tk.Radiobutton(weight_frame, text="lb",
                           variable=weight_unit, value="lb")
lb_button.grid(row=2, column=1)

st_button = tk.Radiobutton(weight_frame, text="St",
                           variable=weight_unit, value="st")
st_button.grid(row=2, column=2)

height_label = tk.Label(root, text="Input your height")
height_label.grid()

height_entry = tk.Entry(root)
height_entry.grid()

height_frame = tk.Frame(root)
height_frame.grid(padx=10, pady=5)

height_unit = tk.StringVar(value="in")

in_button = tk.Radiobutton(height_frame, text="Inches",
                           variable=height_unit, value="in")
in_button.grid(row=7, column=0)
m_button = tk.Radiobutton(height_frame, text="Meters",
                          variable=height_unit, value="m")
m_button.grid(row=7, column=1)

calculate_button = tk.Button(root, text="Calculate",
                             command=calculate_bmi)
calculate_button.grid()

bmi_label = tk.Label(root, text="")
bmi_label.grid()

# Create drop down menu.
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Info', menu=file_menu)
file_menu.add_command(label='BMI ratings', command=show_ratings)
file_menu.add_command(label='Notes', command=notes)
file_menu.add_command(label='Help', command=about)
root.config(menu=menu_bar)


root.mainloop()