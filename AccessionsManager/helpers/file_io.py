import pandas as pd
from odf.opendocument import OpenDocument
import win32api, win32print
from datetime import datetime
from time import sleep
import tempfile
import os


def load_data(data_location: str) -> dict[str, pd.DataFrame]:
    """Load spreadsheet data from file into pandas dataframe

    Returns:
        dict[str, pd.DataFrame]: Dictionary of sheet name keys and sheet data as dataframe
    """
    path = os.path.abspath(data_location)
    excel_data: dict[str, pd.DataFrame] = pd.read_excel(
        path, sheet_name=None, engine="odf", keep_default_na=False, parse_dates=False
    )
    workbook: dict[str, pd.DataFrame] = {}
    for name, data_df in excel_data.items():
        workbook[name] = data_df.map(lambda x: x.strip() if isinstance(x, str) else x)
        workbook[name] = data_df.map(
            lambda x: x.strftime("%d/%m/%Y") if isinstance(x, datetime) else x
        )
        workbook[name].columns = [str(x).title() for x in data_df.columns]
    return workbook


def print_doc(doc: OpenDocument):
    # Create temp file
    filename = tempfile.mktemp(".odt")
    default_printer = win32print.GetDefaultPrinter()

    # Write doc to file
    with open(filename, "wb") as f:
        doc.write(f)
        f.close()
    # Print from shell
    x_code = win32api.ShellExecute(
        0,
        "print",
        filename,
        '/d:"%s"' % default_printer,
        ".",
        0,
    )
    sleep(5)
    file_deleted = False
    while not file_deleted:
        try:
            os.remove(filename)
            file_deleted = True
            print("Temp file deleted")
        except PermissionError:
            pass


def main():
    pass


if __name__ == "__main__":
    main()
