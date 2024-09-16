import ttkbootstrap as ttk
from ttkbootstrap.constants import *  # type: ignore
from ttkbootstrap.tableview import Tableview
from custom_widgets.info_dialog import InfoDialog


class TableFrame(ttk.Frame):
    def __init__(self, data_df, master):
        super().__init__(master)
        self.master = master
        self.data = data_df.to_numpy()
        self.columns = list(data_df.columns)
        self.build_tableview()
        self.build_scrollbars()

    def build_scrollbars(self):
        self.yscroll = ttk.Scrollbar(
            self.tableview.view, orient=VERTICAL, bootstyle=(INFO, ROUND)  # type: ignore
        )
        self.xscroll = ttk.Scrollbar(
            self.tableview.view, orient=HORIZONTAL, bootstyle=(INFO, ROUND)  # type: ignore
        )
        self.tableview.view.configure(yscrollcommand=self.yscroll.set)
        self.tableview.view.configure(xscrollcommand=self.xscroll.set)
        self.xscroll.configure(command=self.tableview.view.xview)
        self.yscroll.configure(command=self.tableview.view.yview)
        self.yscroll.pack(anchor=E, side=RIGHT, fill=Y)
        self.xscroll.pack(anchor=S, side=BOTTOM, fill=X)

    def build_tableview(self):
        self.tableview = Tableview(
            self,
            coldata=self.columns,
            rowdata=self.data,
            autofit=True,
            searchable=True,
            stripecolor=("light blue", None),
            bootstyle=PRIMARY,
        )
        self.tableview.view.bind("<Double-Button-1>", self.double_click)
        self.tableview.pack(anchor=NW, expand=True, fill=BOTH)

    def double_click(self, event):
        row_id = event.widget.identify("row", x=event.x, y=event.y)
        row_data = dict(event.widget.item(row_id).items())
        values = row_data["values"]
        dialog = InfoDialog(
            self, headings=self.columns, values=values, title="Record Information"
        )
        dialog.show()
        self.wait_window(dialog)
