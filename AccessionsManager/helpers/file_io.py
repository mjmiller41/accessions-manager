from pandas import ExcelFile, DataFrame, read_excel
from odf.opendocument import OpenDocument
import win32api, win32print
from datetime import datetime
from time import sleep
import tempfile
import os


def clean_data_in_df(dataframe: DataFrame) -> DataFrame:
    new_df: DataFrame
    new_df = dataframe.map(lambda x: x.strip() if isinstance(x, str) else x)
    new_df = dataframe.map(
        lambda x: x.strftime("%d/%m/%Y") if isinstance(x, datetime) else x
    )
    new_df.columns = [str(x).title() for x in dataframe.columns]
    return new_df


def load_data(data_location: str) -> DataFrame | dict[str, DataFrame]:
    workbook: DataFrame | dict[str, DataFrame] = {}
    path = os.path.abspath(data_location)
    file = ExcelFile(path, engine="odf")
    sheet_names = file.sheet_names
    excel_data: DataFrame | dict[str, DataFrame] = file.parse(
        sheet_name=None,
        keep_default_na=False,
    )  # type: ignore
    if isinstance(excel_data, DataFrame):
        workbook = clean_data_in_df(excel_data)
        workbook.name = sheet_names[0]  # type: ignore
    else:
        for name, data_df in excel_data.items():
            workbook[name] = clean_data_in_df((data_df))
            workbook[name].name = name
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
