import tkinter as tk
import tkinter.messagebox
import customtkinter

# Modes: system (default), light, dark.
customtkinter.set_appearance_mode("system")
# Themes: blue (default), dark-blue, green.
customtkinter.set_default_color_theme("blue")


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

    msg = msg + "\n\nPlease see notes in info menu."

    bmi_result = f"\nYour BMI is: {bmi:.2f}\n\n" + str(msg)
    tk.messagebox.showinfo('BMI Calc result:', bmi_result)


def about():
    tk.messagebox.showinfo('BMI Calc help',
                           '\nInput your weight and'
                           ' choose your preferred\n'
                           'option of kilograms, pounds or stones.\n\n'
                           'Next enter your height in inches or meters.\n'
                           '\nNow click on Calculate to reveal your BMI.\n'
                           '\nThis program is FREEWARE,\nbut remains '
                           '(c) Steve Shambles Feb 2023')


def notes():
    tk.messagebox.showinfo('BMI Calc important notes',
                           'It is important to note that while BMI can be a useful tool for\n'
                           'assessing weight status, it is not a perfect measure.\n\nFor example,\n'
                           'it does not take into account factors like muscle mass or\n'
                           'body composition, which can affect a persons weight but not\n'
                           'necessarily indicate poor health.\n\n'
                           'Additionally, some people may fall into the healthy range but still\n'
                           'have excess body fat, while others may have a high BMI but be\n'
                           'very physically fit.\n\nTherefore, it is always best to consult'
                           ' with a\n'
                           'healthcare professional to determine what a healthy weight range is\n'
                           'for you, based on your individual health'
                           ' and lifestyle factors.')


root = customtkinter.CTk()
root.resizable = (False, False)
root.title("BMI Calc V1.0")


weight_label = customtkinter.CTkLabel(root, font=customtkinter.CTkFont(size=20,
                                      weight="bold"),
                                      text="Input your weight")
weight_label.grid(pady=(10, 0))

weight_entry = customtkinter.CTkEntry(root)
weight_entry.grid(padx=8)

weight_frame = tk.Frame(root)
weight_frame.grid(padx=12)

weight_unit = tk.StringVar(value="st")

kg_button = customtkinter.CTkRadioButton(master=weight_frame,
                                         text="Kilograms", variable=weight_unit,
                                         value="kg")
kg_button.grid(row=2, column=0)

lb_button = customtkinter.CTkRadioButton(master=weight_frame, text="Pounds",
                                         variable=weight_unit, value="lb")
lb_button.grid(row=2, column=1)

st_button = customtkinter.CTkRadioButton(master=weight_frame, text="Stones",
                                         variable=weight_unit, value="st")
st_button.grid(row=2, column=2)

height_label = customtkinter.CTkLabel(root, font=customtkinter.CTkFont(size=20, weight="bold"),
                                      text="Input your height")
height_label.grid(pady=(24, 0))

height_entry = tk.Entry(root)
height_entry.grid()

height_frame = tk.Frame(root)
height_frame.grid(padx=10, pady=5)

height_unit = tk.StringVar(value="in")


in_button = customtkinter.CTkRadioButton(master=height_frame, text="Inches",
                                         variable=height_unit, value="in")
in_button.grid(row=7, column=0)

m_button = customtkinter.CTkRadioButton(master=height_frame, text="Meters",
                                        variable=height_unit, value="m")
m_button.grid(row=7, column=1)

calculate_button = customtkinter.CTkButton(master=root,
                                           font=customtkinter.CTkFont(size=24, weight="bold"),
                                           text="Calculate",
                                           command=calculate_bmi)
calculate_button.grid(pady=(22, 14))


# Create drop down menu.
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Info', menu=file_menu)
file_menu.add_command(label='BMI ratings', command=show_ratings)
file_menu.add_command(label='Notes', command=notes)
file_menu.add_command(label='Help', command=about)
root.config(menu=menu_bar)


root.mainloop()
