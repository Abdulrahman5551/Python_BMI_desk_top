from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

class BMI:

    def __init__(self, root):
        self.root = root
        self.root.geometry('350x500+440+80')
        self.root.title('Calucalte BMI - 1.0')
        self.root.resizable(False, False)

        self.color_screen = {
            "Color 1": "#C75F49",
            "Color 2": "#C79F49",
            "Color 3": "#399286",
            "Color 4": "#394092",
            "Color 5": "#B63C6B"
        }

        # --- Create Variables
        font_family = 'Tajawal-Medium' # Type Font Use 

        self.selected_color_var = StringVar()  # colors
        self.weight_var = StringVar() # weight
        self.height_var = StringVar() # height
        self.result_var = StringVar() # bmi
        self.statu_var = StringVar() # statu

        # Combobox: Select Color
        self.label_select_color = Label(self.root, text='Select Color: ', font=(font_family, 11))
        self.label_select_color.place(x=2, y=5)

        self.combobox_color = ttk.Combobox(self.root, textvariable=self.selected_color_var)
        self.combobox_color['values'] = self.getColor()
        self.combobox_color.place(x=2, y=35)
        self.combobox_color.bind('<<ComboboxSelected>>', self.colorChange)

        # Button: Clear All Entry's
        self.clear_all = Button(self.root, text='Clear', font=(font_family), fg='white' ,bg= 'black', width=13, bd=4, command=self.clearAll)
        self.clear_all.place(x=200, y=35)

        # Label: Weight
        self.label_weight = Label(self.root, text='Weight', font=(font_family, 19))
        self.label_weight.place(x=13, y=80)

        # Label: Height
        self.label_height = Label(self.root, text='Height', font=(font_family, 19))
        self.label_height.place(x=13, y=150)

        # Label: Result BMI
        self.label_result = Label(self.root, text='BMI', font=(font_family, 19))
        self.label_result.place(x=43, y=290)

        # Label: State
        self.label_statu = Label(self.root, text='State', font=(font_family, 19))
        self.label_statu.place(x=43, y=350)

        # Path Photo Image Right Arrow
        self.arrow_1 = PhotoImage(file="C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\BMI_project_3\\images\\right.png")
        self.arrow_2 = PhotoImage(file="C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\BMI_project_3\\images\\right.png")
        self.arrow_3 = PhotoImage(file="C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\BMI_project_3\\images\\right.png")
        self.arrow_4 = PhotoImage(file="C:\\Users\\abdul\\Downloads\\My-Github\\Python_project\\BMI_project_3\\images\\right.png")

        # Place Photo Image Right Arrow
        self.arrow_1_label = Label(self.root, image=self.arrow_1)
        self.arrow_1_label.place(x=106, y=89)
        self.arrow_2_label = Label(self.root, image=self.arrow_2)
        self.arrow_2_label.place(x=106, y=160)
        self.arrow_3_label = Label(self.root, image=self.arrow_3)
        self.arrow_3_label.place(x=106, y=299)
        self.arrow_4_label = Label(self.root, image=self.arrow_4)
        self.arrow_4_label.place(x=106, y=359)

        # Entry: Weight
        self.entry_weight = Entry(self.root, font=(font_family, 16), width=10, justify='center', textvariable=self.weight_var, border=2)
        self.entry_weight.place(x=200, y=101)
        self.entry_weight.focus()

        # Entry: Height
        self.entry_height = Entry(self.root, font=(font_family, 16), width=10, justify='center', textvariable=self.height_var, border=2)
        self.entry_height.place(x=200, y=174)

        # Entry: Result BMI
        self.entry_result = Entry(self.root, font=(font_family, 16), width=10, justify='center', textvariable=self.result_var, state="readonly", border=5)
        self.entry_result.place(x=200, y=316)

        # Entry: State
        self.entry_statu = Entry(self.root, font=(font_family, 16), width=10, justify='center', textvariable=self.statu_var, state="readonly", border=5)
        self.entry_statu.place(x=200, y=378)

        # Button: Calculate And Get BMI
        self.button_caluc = Button(self.root, text='Get BMI', font=(font_family), fg='white' ,bg= 'black',width=25, bd=4, command=self.calculateBMI)
        self.button_caluc.place(x=63, y=230)

        # Frame Bottom [ Black ]
        self.frame = Frame(self.root, bg='black', bd=1, relief=SOLID)
        self.frame.place(x=0, y=450, width=350, height=100)

        # With Run Programm Select Color 1 From Dict
        color_1 = self.color_screen["Color 1"]
        self.root.config(bg=color_1)
        self.label_select_color.config(bg=color_1)
        self.arrow_1_label.config(bg=color_1)
        self.arrow_2_label.config(bg=color_1)
        self.arrow_3_label.config(bg=color_1)
        self.arrow_4_label.config(bg=color_1)

        self.button_caluc.config(bg="black")
        
        self.label_weight.config(bg=color_1)
        self.label_height.config(bg=color_1)
        self.label_result.config(bg=color_1)
        self.label_statu.config(bg=color_1)

    
    # Function Change Color in Cobbmox
    def colorChange(self, event):
        if self.selected_color_var.get() == "Color 1":
            color_1 = self.color_screen["Color 1"]
            self.root.config(bg=color_1)
            self.label_select_color.config(bg=color_1)
            self.arrow_1_label.config(bg=color_1)
            self.arrow_2_label.config(bg=color_1)
            self.arrow_3_label.config(bg=color_1)
            self.arrow_4_label.config(bg=color_1)

            self.button_caluc.config(bg="black")
            
            self.label_weight.config(bg=color_1)
            self.label_height.config(bg=color_1)
            self.label_result.config(bg=color_1)
            self.label_statu.config(bg=color_1)

        elif self.selected_color_var.get() == "Color 2":
            color_2 = self.color_screen["Color 2"]
            self.root.config(bg=color_2)
            self.label_select_color.config(bg=color_2)
            self.arrow_1_label.config(bg=color_2)
            self.arrow_2_label.config(bg=color_2)
            self.arrow_3_label.config(bg=color_2)
            self.arrow_4_label.config(bg=color_2)
            
            self.label_weight.config(bg=color_2)
            self.label_height.config(bg=color_2)
            self.label_result.config(bg=color_2)
            self.label_statu.config(bg=color_2)

        elif self.selected_color_var.get() == "Color 3":
            color_3 = self.color_screen["Color 3"]
            self.root.config(bg=color_3)
            self.label_select_color.config(bg=color_3)
            self.arrow_1_label.config(bg=color_3)
            self.arrow_2_label.config(bg=color_3)
            self.arrow_3_label.config(bg=color_3)
            self.arrow_4_label.config(bg=color_3)
            
            self.label_weight.config(bg=color_3)
            self.label_height.config(bg=color_3)
            self.label_result.config(bg=color_3)
            self.label_statu.config(bg=color_3)

        elif self.selected_color_var.get() == "Color 4":
            color_4 = self.color_screen["Color 4"]
            self.root.config(bg=color_4)
            self.label_select_color.config(bg=color_4)
            self.arrow_1_label.config(bg=color_4)
            self.arrow_2_label.config(bg=color_4)
            self.arrow_3_label.config(bg=color_4)
            self.arrow_4_label.config(bg=color_4)
            
            self.label_weight.config(bg=color_4)
            self.label_height.config(bg=color_4)
            self.label_result.config(bg=color_4)
            self.label_statu.config(bg=color_4)
        
        elif self.selected_color_var.get() == "Color 5":
            color_5 = self.color_screen["Color 5"]
            self.root.config(bg=color_5)
            self.label_select_color.config(bg=color_5)

            self.arrow_1_label.config(bg=color_5)
            self.arrow_2_label.config(bg=color_5)
            self.arrow_3_label.config(bg=color_5)
            self.arrow_4_label.config(bg=color_5)
            
            self.label_weight.config(bg=color_5)
            self.label_height.config(bg=color_5)
            self.label_result.config(bg=color_5)
            self.label_statu.config(bg=color_5)
        
        else:
            pass
    
    # Combbox Values
    def getColor(self):
        list_1 = []

        for x in self.color_screen.keys():
            list_1.append(x)
        return list_1
    
    # Main: Calculate BMI
    def calculateBMI(self):
        getWeight = self.weight_var.get()
        getHeight = self.height_var.get() 

        if len(getWeight) > 0 and len(getWeight) <= 3 and len(getHeight) > 0:
            if getHeight[1] != ".":
                x = str(getHeight[0]+"."+getHeight[1]+getHeight[2])
                getHeight = float(x)
            Bmi = round(float(getWeight) / getHeight ** 2)
            self.result_var.set(Bmi)
            
            if Bmi < 18.5:
                self.statu_var.set("Under Weight")
            elif Bmi < 25:
                self.statu_var.set("Normal")
            elif Bmi < 30:
                self.statu_var.set("Over Weight")
            else:
                self.statu_var.set("Obese")
        
        else:
            messagebox.showerror('Sorry', "Fields Must Be Entered: Weight and Height")
            self.clearAll()
    
    # Clear: All Entry's
    def clearAll(self):
        self.weight_var.set('')
        self.height_var.set('')
        self.result_var.set('')
        self.statu_var.set('')

if __name__ == '__main__':
    root = Tk()
    BMI(root)
    root.mainloop()