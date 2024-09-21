#!.venv/bin/python3.12
# coding=utf-8
import ttkbootstrap as ttk
import ttkbootstrap.utility as tkutil
from ttkbootstrap.constants import *  # type: ignore
import tkinter.font as tkfont
import os
from .custom_widgets import TableFrame, NotebookFrame
from .helpers import file_io, open_doc


class AccessionsManager(ttk.Window):
    def __init__(self, title, theme, logo_path, window_size):
        self.data_location = "accessions.ods"
        super().__init__(title, theme, logo_path, window_size)
        self.hide()  # Hide window during init
        self.workbook = file_io.load_data(self.data_location)
        self.position_center()

        # Set default font size
        self.font = tkfont.nametofont("TkDefaultFont")
        self.font.configure(size=12)

        # Frame container
        self.frame = ttk.Frame(self, padding=5)
        self.frame.pack(anchor=NW)

        # Notebook setup
        self.notebook = NotebookFrame(self.frame)  # type: ignore
        self.notebook.insert_data(self.workbook)
        self.notebook.pack(anchor=NW, expand=True, fill=BOTH)

        # Print Button
        print_button = ttk.Button(
            self.notebook.notebook,
            bootstyle=PRIMARY,  # type: ignore
            text="Print",
            command=self.print_btn_clicked,
        )
        print_button.pack(anchor=NE)

        # Wait 100 ms to avoid unstyled window flicker
        self.update_idletasks()
        self.after(100, self.show)

    def print_btn_clicked(self):
        tableframe = self.notebook.current_tableframe()
        rows: list[list[str]]
        filtered: bool
        criteria: str
        name = tableframe.name
        rows, filtered, criteria = tableframe.get_current_rows()
        columns: list[str] = tableframe.columns
        doc = open_doc.create_rows_odt(rows, columns, name, filtered, criteria)
        # doc.save("item_row_data.odt")
        file_io.print_doc(doc)

    def show(self):
        self.deiconify()
        self.wait_visibility()
        self.lift()
        self.focus_force()
        self.grab_set()

    def hide(self):
        self.withdraw()


def main():
    tkutil.enable_high_dpi_awareness()
    root = AccessionsManager(
        title="Accessions Manager",
        theme="lumen",
        logo_path=os.path.abspath("AccessionsManager/images/hsap_logo_sm.png"),
        window_size=(1280, 720),
    )
    root.mainloop()


if __name__ == "__main__":
    main()
