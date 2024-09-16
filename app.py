#!.venv/bin/python3.12
# coding=utf-8

import ttkbootstrap as ttk
import ttkbootstrap.utility as tkutil
from ttkbootstrap.icons import Emoji, Icon
from ttkbootstrap.constants import *  # type: ignore
import tkinter as tk
import tkinter.font as tkfont
import pandas as pd
import os.path as path
import custom_widgets as cust


def load_data() -> dict[str, pd.DataFrame]:
    workbook_path = "data/accessions.ods"
    path_ = path.abspath(workbook_path)
    excel_data: dict[str, pd.DataFrame] = pd.read_excel(
        path_, sheet_name=None, engine="odf", keep_default_na=False
    )
    workbook: dict[str, pd.DataFrame] = {}
    for name, data_df in excel_data.items():
        workbook[name] = data_df.map(lambda x: x.strip() if isinstance(x, str) else x)
        workbook[name].columns = [str(x).title() for x in data_df.columns]
    return workbook


def show(root):
    root.deiconify()
    root.wait_visibility()
    root.lift()
    root.focus_force()
    root.grab_set()


def run_app() -> None:
    title = "Accessions Manager"
    theme = "my_lumen"
    logo_path = "images/hsap_logo_sm.png"
    window_size = (1280, 720)
    window_settings = (title, theme, logo_path, window_size)
    tkutil.enable_high_dpi_awareness()

    # Root window ######################################################################
    root = ttk.Window(*window_settings)
    root.withdraw()
    root.position_center()

    # Set default font size
    font = tkfont.nametofont("TkDefaultFont")
    font.configure(size=12)

    frame = ttk.Frame(root, padding=5)
    frame.pack(anchor=CENTER, expand=True, fill=BOTH)

    # Notebook setup
    notebook = ttk.Notebook(frame, bootstyle=PRIMARY)  # type: ignore
    notebook.pack(anchor=NW, expand=True, fill=BOTH)

    # Menu button setup
    folder = Emoji.get("open file folder")
    disk = Emoji.get("floppy disk")
    menu_btn = ttk.Menubutton(notebook, bootstyle=PRIMARY, text="Menu", direction="below")  # type: ignore
    menu_btn.pack(anchor=NE, fill=NONE)
    menu = tk.Menu(menu_btn, tearoff=0)  # type: ignore
    menu.add_command(label=f"{folder} Open Workbook")  # type: ignore
    menu.add_command(label=f"{disk} Save Workbook")  # type: ignore
    menu_btn["menu"] = menu  # type: ignore

    # Fill notebook tabs with workbook data
    workbook = load_data()
    for name, data_df in workbook.items():
        tree_frame = cust.TableFrame(master=notebook, data_df=data_df)
        tree_frame.pack(anchor=NW, expand=True, fill=BOTH)
        notebook.add(tree_frame, text=name, sticky=NSEW)

    # Wait 100 ms to avoid unstyled window flicker
    root.after(100, show, root)
    root.mainloop()
    # End root window ######################################################################


def main() -> None:
    """main function"""
    run_app()


if __name__ == "__main__":
    main()
