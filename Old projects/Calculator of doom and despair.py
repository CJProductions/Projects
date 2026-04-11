import tkinter as tk

def buttonClicked():
    print("BUTTON!")
def main():
    calculator = tk.Tk()
    calculator.geometry("400x600")
    calculator.title("Calculator")
    calculator.background(bg="grey")
    message = tk.Message(calculator, text="Doohickey")
    message.pack()
    message.config(bg="lightblue")
    button1 = tk.Button(calculator, text="1", command=lambda:buttonClicked(), width=8, height=8 )
    button1.pack(padx=120, pady=30)
    button1.place()
    calculator.mainloop()
if __name__ == "__main__":
    main()