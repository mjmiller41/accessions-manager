from odf.opendocument import OpenDocument, Text
from odf.style import PageLayout
from odf.style import MasterPage
from odf.style import PageLayoutProperties
from odf.style import Style
from odf.style import TextProperties
from odf.style import ParagraphProperties
from odf.style import DefaultStyle


HYPERLINK_PROPERTIES_ATTRIBUTES = {
    "color": "#0000FF",
    "textunderlinetype": "single",
    "textunderlinestyle": "solid",
    "textunderlinewidth": "auto",
}


class MyStyles:
    def __init__(self, document: OpenDocument):
        super().__init__()
        # Heading Style
        self.heading = Style(
            name="Heading 1",
            parentstylename="Standard",
            family="paragraph",
        )
        heading_prop = TextProperties(
            attributes={"fontsize": "24pt", "fontweight": "bold"}
        )
        self.heading.addElement(heading_prop)
        document.automaticstyles.addElement(self.heading)

        # Bold style
        self.bold = Style(
            name="Bold",
            parentstylename="Standard",
            family="paragraph",
        )
        boldprop = TextProperties(fontweight="bold")
        self.bold.addElement(boldprop)
        document.automaticstyles.addElement(self.bold)

        # Centered Text Style
        self.centered = Style(
            name="Centered",
            parentstylename="Standard",
            family="paragraph",
        )
        self.centered.addElement(ParagraphProperties(textalign="center"))
        document.automaticstyles.addElement(self.centered)

        # Hyperlink
        hyperlink_properties = TextProperties(
            attributes={
                "color": "#0000FF",
                "textunderlinetype": "single",
                "textunderlinestyle": "solid",
                "textunderlinewidth": "auto",
            },
        )
        self.hyperlink = Style(
            name="Hyperlink",
            parentstylename="Standard",
            family="paragraph",
        )
        self.hyperlink.addElement(hyperlink_properties)
        document.automaticstyles.addElement(self.hyperlink)


class TextDocument(OpenDocument):
    def __init__(self, page_orientation: str = "portrait", margins: str = "0.5in"):
        super().__init__("application/vnd.oasis.opendocument.text")
        # self.document = OpenDocumentText()
        self.text = Text()
        self.body.addElement(self.text)

        # Default Text Syle
        default_style = DefaultStyle(family="paragraph")
        text_properties = TextProperties(
            fontfamily="Liberation Sans",
            fontsize="12pt",
            fontweight="normal",
        )
        default_style.addElement(text_properties)
        self.styles.addElement(default_style)

        # Page Layout
        page_layout_style = PageLayout(name="pagelayoutstyle")
        page_layout_style.addElement(
            PageLayoutProperties(
                pagewidth="11in",
                pageheight="8.5in",
                printorientation=page_orientation,
                margintop=margins,
                marginleft=margins,
                marginbottom=margins,
                marginright=margins,
                numformat="1",
                writingmode="lr-tb",
            )
        )
        self.automaticstyles.addElement(page_layout_style)
        # Master Page
        master_page = MasterPage(name="Standard", pagelayoutname=page_layout_style)
        self.masterstyles.addElement(master_page)

        # # Footer
        # footer = Footer()
        # footer_paragraph = P()
        # footer_paragraph.addElement(PageNumber(text="1"))
        # footer.addElement(footer_paragraph)
        # master_page.addElement(footer)

        # # Header
        # header = Header()
        # header_paragraph = P(text="Training name", stylename=styles.centered)
        # header.addElement(header_paragraph)
        # master_page.addElement(header)
        # # Body
        # self.document.text.addElement(  # type: ignore
        #     P(text="Test text goes here", stylename=styles.plain_text)
        # )

        # span = Span(text="hyperlink", stylename=styles.hyperlink)
        # hyperlink = A(href="https://www.cnn.com")
        # hyperlink.addElement(span)
        # paragraph = P()
        # paragraph.addElement(hyperlink)
        # self.document.text.addElement(paragraph)  # type: ignore
