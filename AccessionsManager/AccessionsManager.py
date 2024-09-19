#!.venv/bin/python3.12
# coding=utf-8
"""App to manage accessions data for museums

Returns:
    None: Creates GUI application
"""

import pandas as pd
import ttkbootstrap as ttk
import ttkbootstrap.utility as tkutil
from ttkbootstrap.icons import Emoji
from ttkbootstrap.constants import *  # type: ignore
import tkinter as tk
import tkinter.font as tkfont
import os
from datetime import datetime
from .custom_widgets.table_frame import TableFrame
from .helpers.file_io import load_data


# logo_path = "AccessionsManager/images/hsap_logo_sm.png"
# self.window_settings = (title, theme, logo_path, window_size)
# def run_app() -> None:
class AccessionsManager(ttk.Window):
    def __init__(self, title, theme, logo_path, window_size):
        self.data_location = "accessions.ods"
        super().__init__(title, theme, logo_path, window_size)
        self.hide()  # Hide window durring init
        self.workbook = load_data(self.data_location)
        self.position_center()

        # Set default font size
        self.font = tkfont.nametofont("TkDefaultFont")
        self.font.configure(size=12)

        # Frame container
        self.frame = ttk.Frame(self, padding=5)
        self.frame.pack(anchor=CENTER, expand=True, fill=BOTH)

        # Menu button setup
        folder_icon = Emoji.get("open file folder")
        disk_icon = Emoji.get("floppy disk")
        self.menu_btn = ttk.Menubutton(self.frame, bootstyle=PRIMARY, text="Menu", direction="below")  # type: ignore
        self.menu_btn.pack(anchor=NE, fill=NONE)
        self.menu = tk.Menu(self.menu_btn, tearoff=0)  # type: ignore
        self.menu.add_command(label=f"{folder_icon} Open Workbook")  # type: ignore
        self.menu.add_command(label=f"{disk_icon} Save Workbook")  # type: ignore
        self.menu_btn["menu"] = self.menu  # type: ignore

        # Notebook setup
        self.notebook = ttk.Notebook(self.frame, bootstyle=PRIMARY)  # type: ignore
        self.notebook.pack(anchor=NW, expand=True, fill=BOTH)

        # Fill notebook tabs with workbook data
        for name, data_df in self.workbook.items():
            table_frame = TableFrame(master=self.notebook, data_df=data_df)
            table_frame.pack(anchor=NW, expand=True, fill=BOTH)
            self.notebook.add(table_frame, text=name, sticky=NSEW)

        # Wait 100 ms to avoid unstyled window flicker
        self.update_idletasks()
        self.after(100, self.show)

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
