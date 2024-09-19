from odf.opendocument import OpenDocumentText, OpenDocument
from odf.style import Style, TextProperties
from odf.text import H, P, Span


def create_info_odt(item_info: zip) -> OpenDocument:
    textdoc = OpenDocumentText()

    # Heading Style
    h1 = Style(name="Heading 1", family="paragraph")
    h1_prop = TextProperties(attributes={"fontsize": "24pt", "fontweight": "bold"})
    h1.addElement(h1_prop)
    textdoc.automaticstyles.addElement(h1)

    # Bold style
    bold = Style(name="Bold", family="text")
    boldprop = TextProperties(fontweight="bold")
    bold.addElement(boldprop)
    textdoc.automaticstyles.addElement(bold)

    # Text
    h = H(outlinelevel=1, stylename=h1, text="Accession Info.")
    textdoc.text.addElement(h)  # type: ignore
    for item in item_info:
        p = P()
        heading = Span(text=f"{item[0]}: ", stylename=bold)
        p.addElement(heading)
        info = Span(text=f"{item[1]}\n")
        p.addElement(info)
        textdoc.text.addElement(p)  # type: ignore
    return textdoc
