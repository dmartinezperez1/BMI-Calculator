from tkinter import *

root = Tk()
root.geometry("400x350") #Size of GUI window
root.title("BMI Calculator")
descri = Label(root, text = "Please fill out the following information", font = ("Arial", 10)).pack()

L1 = Label(root, text = "Weight in Lbs:")
L1.pack()
weight = Entry(root)
weight.pack()
L2 = Label(root, text = "Height in inchs:")
L2.pack()
height = Entry(root)
height.pack()


#Function to calculate BMI
def calculate():
    #Convert weight from pounds to kilograms
    weightlb = int(weight.get())
    weightkg = weightlb * .454

    #Convert height from inches to meters
    heightin = int(height.get())
    heightm = heightin * .0254

    #Formula for BMI is (weight in kg)/(height in m squared)
    heightsqrd = heightm * heightm
    bmi = weightkg / heightsqrd

    bmiOutput = Label(root, text = str(round(bmi,2))).pack()

    if bmi < 18.5:
        status = "You are underweight"
    elif 18.5 < bmi < 24.9:
        status = "You are at a healthy weight"
    elif 25 < bmi < 29.9:
        status = "You are slighty overweight"
    elif bmi > 30:
        status = "You are obese"
    
    statusOutput = Label(root, text = status).pack()


#Once results are entered, this button will calculate BMI and present in the GUI
widget = Button(root, text = 'Calculate!', command = calculate).pack()
root.mainloop()