from django.db import models
from django.utils.translation import gettext_lazy as _


class ArticleCategory(models.TextChoices):
    DEV = 'Dev', _('Dev')
    DEVOPS = 'DevOps', _('DevOps')
    FEEL_GOOD = 'Feel Good', _('Feel Good')
    BIM = 'BIM', _('BIM')
    MAKERS = 'Makers', _('Makers')
    AGILE = 'Agile', _('Agile')
    UX_UI = 'UX/UI', _('UX/UI')
    DATA = 'Data', _('Data')
    SSI = 'SSI', _('SSI')
    INDUS = 'Industrie', _('Industrie')


# Create your models here.
class Article(models.Model):

    title = models.CharField(_('Title'), max_length=50)
    category = models.TextField(_('Category'), choices=ArticleCategory.choices)
    content = models.TextField(_('Content'))
    image = models.ImageField(default='background-image.png')

    def img_src(self):
        return f'images/{self.image}'
