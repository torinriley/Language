import re

class SyntaxHighlighter:
    def __init__(self, editor):
        self.text_editor = editor.text_editor
        self.text_editor.tag_configure("keyword", foreground="#FF7B72", font=("Courier New", 14, "bold")) 
        self.text_editor.tag_configure("variable", foreground="#79C0FF", font=("Courier New", 14)) 
        self.text_editor.tag_configure("number", foreground="#A5D6FF", font=("Courier New", 14)) 

    def apply_highlighting(self, event=None):
        """Applies syntax highlighting."""
        self.text_editor.tag_remove("keyword", "1.0", "end")
        self.text_editor.tag_remove("variable", "1.0", "end")
        self.text_editor.tag_remove("number", "1.0", "end")

        code = self.text_editor.get("1.0", "end")

        keyword_pattern = r'\b(print|if|while|assign)\b'
        variable_pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
        number_pattern = r'\b\d+\b'

        for pattern, tag in [
            (keyword_pattern, "keyword"),
            (variable_pattern, "variable"),
            (number_pattern, "number")
        ]:
            for match in re.finditer(pattern, code):
                start = f"1.0 + {match.start()} chars"
                end = f"1.0 + {match.end()} chars"
                self.text_editor.tag_add(tag, start, end)