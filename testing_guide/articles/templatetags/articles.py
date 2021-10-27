import markdown
from django import template
from articles.models import ArticleCategory
register = template.Library()


@register.simple_tag
def article_category():
    return ArticleCategory.choices


@register.filter
def article_color(value):
    colors = {
        ArticleCategory.DEV: "#8d0076",
        ArticleCategory.DEVOPS: "#d34a4a",
        ArticleCategory.FEEL_GOOD: "#4a63d3",
        ArticleCategory.BIM: "#4ab8d3",
        ArticleCategory.MAKERS: "#45d445",
        ArticleCategory.AGILE: "#d2d445",
        ArticleCategory.UX_UI: "#db8e46",
        ArticleCategory.DATA: "#ac46db",
        ArticleCategory.SSI: "#6146db",
        ArticleCategory.INDUS: "#2048a0",
    }
    return colors[value]


@register.filter
def htmlize(value):
    return markdown.markdown(value)
