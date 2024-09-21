from ttkbootstrap.scrolled import ScrolledText
import tkinter.font as tkFont


class RichText(ScrolledText):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)  # bootstyle="primary",

        default_font = tkFont.nametofont(self.text.cget("font"))

        em = default_font.measure("m")
        default_size = default_font.cget("size")
        bold_font = tkFont.Font(**default_font.configure())  # type: ignore
        italic_font = tkFont.Font(**default_font.configure())  # type: ignore
        h1_font = tkFont.Font(**default_font.configure())  # type: ignore

        bold_font.configure(weight="bold")
        italic_font.configure(slant="italic")
        h1_font.configure(size=int(default_size * 2), weight="bold")

        self.tag_configure("bold", font=bold_font)  # type: ignore
        self.tag_configure("italic", font=italic_font)  # type: ignore
        self.tag_configure("h1", font=h1_font, spacing3=default_size)  # type: ignore

        lmargin2 = em + default_font.measure("\u2022 ")
        self.tag_configure("bullet", lmargin1=em, lmargin2=lmargin2)  # type: ignore

    def insert_bullet(self, index, text):
        self.insert(index, f"\u2022 {text}", "bullet")  # type: ignore
