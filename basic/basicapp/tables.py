import django_tables2 as tables
from .models import CharactorModel
from django_tables2.utils import A
from django.utils.html import format_html

class ImageColumn(tables.Column):
    def render(self, value):
        return format_html('<a href="{}">画像リンク</a>', value)

class PageColumn(tables.Column):
    def render(self, value):
        return format_html('<a href="{}">ページリンク</a>', value)
    
class CharactorTable(tables.Table):
    image_link = ImageColumn()
    page_link = PageColumn()
    
    class Meta:
        model = CharactorModel
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "gender", "feature", "image_link", "page_link")