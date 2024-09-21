import ttkbootstrap as ttk
from ttkbootstrap import Toplevel
from ttkbootstrap.constants import *  # type: ignore
from .RichText import RichText
from AccessionsManager.helpers import open_doc, file_io


class InfoDialog(Toplevel):
    def __init__(self, master, headings, values, title, **kwargs):
        super().__init__(title=title, **kwargs)
        self.hide()  # Hide window until self.show()
        self.wm_minsize(width=500, height=450)
        self.master = master
        self.headings = headings
        self.values = values
        self.title = title
        self.insert_text_widget()
        self.insert_close_btn()
        self.insert_print_btn()
        self.configure(pady=10, padx=10)
        self.set_geometry()

    def insert_text_widget(self):
        self.text = RichText(self, wrap=WORD)
        self.text.place(anchor=NW, relx=0, rely=0, relheight=0.85, relwidth=1)
        for index, heading in enumerate(self.headings):
            self.text.insert(END, f"{heading}:", "bold")  # type: ignore
            self.text.insert(END, f"\t{self.values[index]}\n")  # type: ignore

    def insert_close_btn(self):
        self.close_btn = ttk.Button(self, text="Close", command=self.on_close)
        self.close_btn.place(anchor=SW, relx=0.2, rely=0.98)

    def insert_print_btn(self):
        self.print_btn = ttk.Button(self, text="Print", command=self.on_print)
        self.print_btn.place(anchor=SE, relx=0.8, rely=0.98)

    def set_geometry(self):
        self.update_idletasks()
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = int((screen_width / 2) - self.width / 2)
        y = int((screen_height / 2) - self.height / 2)
        self.geometry(f"+{x}+{y}")

    def show(self):
        self.deiconify()
        self.wait_visibility()
        self.lift()
        self.focus_force()
        self.grab_set()

    def hide(self):
        self.withdraw()
        self.transient(self.master)  # type: ignore

    def on_close(self):
        self.grab_release()
        self.destroy()

    def on_print(self):
        item_info = zip(self.headings, self.values)
        o_doc = open_doc.create_info_odt(item_info)
        file_io.print_doc(o_doc)
