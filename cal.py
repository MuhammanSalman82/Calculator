import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("SALMAN-CALCULATOR")
        self.root.configure(bg='blue')  # Set background color to blue
        self.root.geometry("350x580")   # Increased height to accommodate the name
        
        self.expression = ""

        # Entry widget to display input/output
        self.display = tk.Entry(self.root, font=("Arial", 18))
        self.display.grid(row=0, column=0, columnspan=4, pady=20, padx=10, ipady=10)

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 5, 1), ('+', 4, 3),
            ('C', 5, 0), ('←', 4, 2)  # '0' and 'backspace' buttons corrected
        ]

        for (text, row, column) in buttons:
            button = tk.Button(self.root, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, ipadx=20, ipady=10, padx=5, pady=5, sticky=tk.NSEW)

        # Adding the '+' button separately
        plus_button = tk.Button(self.root, text='+', font=("Arial", 18), command=lambda: self.on_button_click('+'))
        plus_button.grid(row=4, column=3, ipadx=20, ipady=10, padx=5, pady=5, sticky=tk.NSEW)

        # Name label at the bottom
        self.name_label = tk.Label(self.root, text="Prepared by\n M.Salman-NED", fg="black", bg="blue", font=("Arial", 20, "italic","bold"))
        self.name_label.grid(row=6, column=0, columnspan=4, pady=10)

    def on_button_click(self, text):
        if text == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        elif text == 'C':
            self.expression = ""
        elif text == '←':  # Backspace functionality
            self.expression = self.expression[:-1]
        else:
            self.expression += text

        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
