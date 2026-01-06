# digital_clock.py
import tkinter as tk
from time import strftime


class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.geometry("450x180")
        self.root.configure(bg="black")
        self.root.resizable(False, False)

        self.time_label = tk.Label(
            root, font=("Segoe UI", 48, "bold"), background="black", foreground="cyan"
        )
        self.time_label.pack(pady=10)

        self.date_label = tk.Label(
            root, font=("Segoe UI", 16), background="black", foreground="white"
        )
        self.date_label.pack()

        self.update_clock()

    def update_clock(self):
        current_time = strftime("%I:%M:%S %p")  # 12-hour format
        current_date = strftime("%A, %d %B %Y")

        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)

        self.root.after(1000, self.update_clock)


if __name__ == "__main__":
    root = tk.Tk()
    DigitalClock(root)
    root.mainloop()
