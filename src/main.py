import tkinter as tk
from editor import Editor
from output_console import OutputConsole
from syntax_highlighter import SyntaxHighlighter
from interpreter import PulseInterpreter

class PulseIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("Pulse IDE")

        self.editor = Editor(root)
        self.output_console = OutputConsole(root)
        self.highlighter = SyntaxHighlighter(self.editor)

        self.editor.set_event(self.highlighter.apply_highlighting)

        self.button_frame = tk.Frame(root, bg="#2b2b2b")
        self.button_frame.pack(side=tk.TOP, fill=tk.X)
        self.run_button = tk.Button(
            self.button_frame,
            text="Run",
            command=self.run_code,
            bg="#28a745",
            fg="white",
            font=("Helvetica", 12, "bold"),
            padx=10,
            pady=5
        )
        self.run_button.pack(side=tk.RIGHT, padx=10, pady=5)

    def run_code(self):
        """Executes the code."""
        code = self.editor.get_code()
        if not code:
            self.output_console.display_output("No code to run!")
            return

        try:
            tokens = PulseInterpreter.tokenize(code)
            ast = PulseInterpreter.parse(tokens)
            output = PulseInterpreter.execute_ast(ast)
            self.output_console.display_output(output)
        except Exception as e:
            self.output_console.display_output(f"Error: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    ide = PulseIDE(root)
    root.mainloop()