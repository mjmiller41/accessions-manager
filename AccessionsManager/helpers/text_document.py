from odf.opendocument import OpenDocument, Text
from odf.style import (
    PageLayout,
    MasterPage,
    PageLayoutProperties,
    Style,
    TextProperties,
    ParagraphProperties,
    DefaultStyle,
)


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

        # Bold text style
        self.bold_text = Style(
            name="Bold_text",
            parentstylename="Standard",
            family="text",
        )
        boldprop = TextProperties(fontweight="bold")
        self.bold_text.addElement(boldprop)
        # Bold paragraph style
        document.automaticstyles.addElement(self.bold_text)
        self.bold_paragraph = Style(
            name="Bold_paragraph",
            parentstylename="Standard",
            family="paragraph",
        )
        boldprop = TextProperties(fontweight="bold")
        self.bold_paragraph.addElement(boldprop)
        document.automaticstyles.addElement(self.bold_paragraph)

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
        self.page_orientation = page_orientation
        self.margins = margins
        self.page_width = "8.5in"
        self.page_height = "11in"

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
        if self.page_orientation == "landscape":
            self.page_width = "11in"
            self.page_height = "8.5in"
        page_layout_style.addElement(
            PageLayoutProperties(
                pagewidth=self.page_width,
                pageheight=self.page_height,
                printorientation=self.page_orientation,
                margintop=self.margins,
                marginleft=self.margins,
                marginbottom=self.margins,
                marginright=self.margins,
                numformat="1",
                writingmode="lr-tb",
            )
        )
        self.automaticstyles.addElement(page_layout_style)

        # Master Page
        master_page = MasterPage(name="Standard", pagelayoutname=page_layout_style)
        self.masterstyles.addElement(master_page)

    # def set_footer(self):
    #     # Footer
    #     footer = Footer()
    #     footer_paragraph = P()
    #     footer_paragraph.addElement(PageNumber(text="1"))
    #     footer.addElement(footer_paragraph)
    #     master_page.addElement(footer)

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
