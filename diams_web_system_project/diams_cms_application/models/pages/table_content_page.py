from wagtail.admin.panels import FieldPanel
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.fields import StreamField

from diams_cms_application.models import AContentPage

table_options = {
    'contextMenu': [
        'row_above',
        'row_below',
        '---------',
        'col_left',
        'col_right',
        '---------',
        'remove_row',
        'remove_col',
        '---------',
        'undo',
        'redo',
        '---------',
        'copy',
        'cut',
        '---------',
        'alignment',
    ],
}


class CustomTableBlock(TableBlock):
    class Meta:
        template = "diams_cms_application/blocks/table.html"


class TableContentPage(AContentPage):
    template = "diams_cms_application/table_content_page.html"

    body = StreamField(
        [("table", CustomTableBlock(table_options=table_options))], null=True, blank=True)

    content_panels = AContentPage.content_panels + [
        FieldPanel("body"),
    ]
