import tkinter as tk

class OutputConsole:
    def __init__(self, parent):
        self.output_container = tk.Text(
            parent,
            height=10,
            font=("Courier New", 14),
            padx=5,
            pady=5,
            bg="black",
            fg="white",
            state=tk.DISABLED,
            highlightthickness=0
        )
        self.output_container.pack(fill=tk.BOTH)

    def display_output(self, output):
        """Displays the output in the console."""
        self.output_container.config(state=tk.NORMAL)
        self.output_container.delete("1.0", tk.END)
        self.output_container.insert("1.0", output)
        self.output_container.config(state=tk.DISABLED)
        