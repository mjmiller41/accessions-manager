import ttkbootstrap as ttk
from ttkbootstrap import Toplevel
from ttkbootstrap.constants import *  # type: ignore
from custom_widgets.rich_text import RichText


class InfoDialog(Toplevel):
    def __init__(self, master, headings, values, title, **kwargs):
        super().__init__(title=title, **kwargs)
        self.master = master
        self.headings = headings
        self.values = values
        self.title = title
        # Hide window until show() called
        self.withdraw()
        self.transient(self.master)  # type: ignore
        self.set_geometry()
        self.build_text_widget()
        self.build_btn()

    def build_btn(self):
        self.ok = ttk.Button(self, text="OK", command=self.onOk)
        b_style = ttk.Style()
        b_style.configure("TButton", padding=[5, 0, 5, 3])
        self.ok.pack(anchor=S, expand=True, pady=15)

    def build_text_widget(self):
        self.text = RichText(self, wrap=WORD)
        self.text.pack(anchor=N, fill=X)
        for index, heading in enumerate(self.headings):
            self.text.insert(END, f"{heading}:", "bold")  # type: ignore
            self.text.insert(END, f"\t{self.values[index]}\n")  # type: ignore

    def set_geometry(self, w: int = 500, h: int = 500):
        x = self.master.winfo_screenwidth()
        y = self.master.winfo_screenheight()
        x = int((x / 2) - w / 2)
        y = int((y / 2) - h / 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

    def show(self):
        self.deiconify()
        self.wait_visibility()
        self.lift()
        self.focus_force()
        self.grab_set()

    def onOk(self):
        self.grab_release()
        self.destroy()
