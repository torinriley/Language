import tkinter as tk


class Editor:
    def __init__(self, parent):
        self.parent = parent

        self.frame = tk.Frame(self.parent)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.line_numbers = tk.Text(
            self.frame,
            width=4,
            font=("Courier New", 14),
            padx=5,
            pady=5,
            bg="#2b2b2b",
            fg="white",
            state=tk.DISABLED,
            relief=tk.FLAT
        )
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        self.text_editor = tk.Text(
            self.frame,
            wrap="word",
            font=("Courier New", 14),
            padx=5,
            pady=5,
            bg="#1e1e1e",
            fg="white",
            insertbackground="white",
            highlightthickness=0
        )
        self.text_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        
        self.scrollbar = tk.Scrollbar(self.frame, command=self._on_scroll)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_editor.config(yscrollcommand=self.scrollbar.set)

        
        self.text_editor.bind("<KeyRelease>", self.update_line_numbers)
        self.text_editor.bind("<MouseWheel>", self._on_scroll)

    def update_line_numbers(self, event=None):
        """Updates the line numbers in the editor."""
        self.line_numbers.config(state=tk.NORMAL)
        self.line_numbers.delete("1.0", tk.END)

        lines = int(self.text_editor.index("end-1c").split(".")[0])
        line_numbers_string = "\n".join(str(i) for i in range(1, lines + 1))

        self.line_numbers.insert("1.0", line_numbers_string)
        self.line_numbers.config(state=tk.DISABLED)

    def get_code(self):
        """Gets the text from the editor."""
        return self.text_editor.get("1.0", tk.END).strip()

    def set_event(self, event_func):
        """Bind external events to the editor."""
        self.text_editor.bind("<KeyRelease>", lambda event: (event_func(event), self.update_line_numbers()))

    def _on_scroll(self, *args):
        """Scrolls the line numbers along with the editor."""
        self.text_editor.yview(*args)
        self.line_numbers.yview(*args)
        self.update_line_numbers()