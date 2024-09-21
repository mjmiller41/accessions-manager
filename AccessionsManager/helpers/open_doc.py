from odf.opendocument import OpenDocument
from odf.style import Style, ParagraphProperties
from odf.style import TableColumnProperties
from odf.style import TableCellProperties
from odf.table import (
    Table,
    TableColumn,
    TableRow,
    TableCell,
    TableHeaderRows,
)
from odf.text import H, P, Span
from .text_document import TextDocument, MyStyles


def create_info_odt(item_info: zip) -> OpenDocument:
    textdoc = TextDocument(page_orientation="portrait")
    styles = MyStyles(textdoc)

    # Text
    h = H(outlinelevel=1, stylename=styles.heading, text="Accession Info.")
    textdoc.text.addElement(h)  # type: ignore
    for item in item_info:
        p = P()
        heading = Span(text=f"{item[0]}: ", stylename=styles.bold_text)
        p.addElement(heading)
        info = Span(text=f"{item[1]}\n")
        p.addElement(info)
        textdoc.text.addElement(p)  # type: ignore
    return textdoc


def create_rows_odt(
    rows: list[list[str]],
    columns: list[str],
    name: str,
    filtered: bool = False,
    criteria: str = "",
) -> OpenDocument:
    textdoc = TextDocument(page_orientation="landscape")
    styles = MyStyles(textdoc)

    table_cell_style = Style(name="table_cell_style", family="table-cell")
    table_cell_style.addElement(
        TableCellProperties(borderbottom="0.75pt solid #000000")
    )
    textdoc.automaticstyles.addElement(table_cell_style)

    table_header_cell_style = Style(name="table_header_cell_style", family="table-cell")
    table_header_cell_style.addElement(
        TableCellProperties(border="0.75pt solid #000000")
    )
    textdoc.automaticstyles.addElement(table_header_cell_style)

    widthshort = Style(name="Wshort", family="table-column")
    widthshort.addElement(TableColumnProperties(columnwidth="1.0in"))
    textdoc.automaticstyles.addElement(widthshort)

    widthwide = Style(name="Wwide", family="table-column")
    widthwide.addElement(TableColumnProperties(columnwidth="3.0in"))
    textdoc.automaticstyles.addElement(widthwide)

    num_columns = len(columns)
    table = Table()
    table.addElement(
        TableColumn(numbercolumnsrepeated=num_columns - 1, stylename=widthshort)
    )
    table.addElement(TableColumn(numbercolumnsrepeated=1, stylename=widthwide))

    # Text
    heading = ""
    if filtered:
        heading = f"{name}: {criteria}"
    else:
        heading = name
    h = H(outlinelevel=1, stylename=styles.heading, text=heading)
    textdoc.text.addElement(h)  # type: ignore

    th = TableHeaderRows()
    tr = TableRow()
    for heading in columns:
        tc = TableCell(stylename="table_header_cell_style")
        tr.addElement(tc)
        p = P(stylename=styles.bold_paragraph, text=heading)
        tc.addElement(p)
    th.addElement(tr)
    table.addElement(th)

    for row in rows:
        tr = TableRow()
        for val in row:
            tc = TableCell(stylename="table_cell_style")
            tr.addElement(tc)
            p = P(text=val)
            tc.addElement(p)
        table.addElement(tr)
    textdoc.text.addElement(table)  # type: ignore
    return textdoc
