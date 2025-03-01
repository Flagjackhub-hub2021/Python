import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=25, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        digits = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
        operators = ['/', '*', '-', '+', '=', 'C']

        row = 1
        col = 0
        for digit in digits:
            tk.Button(master, text=digit, width=5, height=2,
                      command=lambda digit=digit: self.add_to_display(digit)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 2:
                col = 0
                row += 1

        for operator in operators:
            tk.Button(master, text=operator, width=5, height=2,
                      command=lambda operator=operator: self.handle_operator(operator)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def add_to_display(self, digit):
        self.display.insert(tk.END, digit)

    def handle_operator(self, operator):
        if operator == 'C':
            self.display.delete(0, tk.END)
        elif operator == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, operator)

root = tk.Tk()
calc = Calculator(root)


root.mainloop()
