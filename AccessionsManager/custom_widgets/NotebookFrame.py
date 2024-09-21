#!.venv/Scripts/python
# coding=utf-8
"""
Copyright 2024, Michael Joseph Miller #

This file is part of AccessionsManager.

AccessionsManager is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License,
or (at your option) any later version.

AccessionsManager is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License
along with AccessionsManager. If not,
see <https: //www.gnu.org/licenses/>.
"""
from ttkbootstrap import Frame, Notebook, Style
from ttkbootstrap.constants import *  # type: ignore
from pandas import DataFrame
from .TableFrame import TableFrame


class NotebookFrame(Frame):
    def __init__(self, master):
        super().__init__()
        self.notebook = Notebook(self, bootstyle=PRIMARY)  # type: ignore
        self.notebook.pack(anchor=NW, expand=True, fill=BOTH)
        self.tableframes = []

    def insert_data(self, data: DataFrame | dict[str, DataFrame]):
        if isinstance(data, DataFrame):
            self.add_tab(data)
            self.set_tab_style()
        else:
            for dataframe in data.values():
                self.add_tab((dataframe))

    def add_tab(self, dataframe: DataFrame):
        tableframe = TableFrame(master=self.notebook, data_df=dataframe)
        tableframe.pack(anchor=NW, expand=True, fill=BOTH)
        self.notebook.add(tableframe, text=dataframe.name, sticky=NSEW)  # type: ignore
        self.tableframes.append(tableframe)

    def current_tableframe(self) -> TableFrame:
        tab = self.notebook.index("current")
        return self.notebook.winfo_children()[tab]

    def set_tab_style(self):
        style = Style()
        style.map(
            "primary.TNotebook.Tab",
            background=[("selected", "#158cba")],
            lightcolor=[("selected", "#158cba")],
            bordercolor=[("selected", "#158cba")],
            padding=[("selected", (6, 5))],
            foreground=[("selected", "#F6F6F6")],
        )


def main() -> None: ...


if __name__ == "__main__":
    main()
