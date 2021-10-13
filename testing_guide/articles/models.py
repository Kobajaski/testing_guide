from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User


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
    title = models.CharField(_('Title'), max_length=32)
    category = models.TextField(_('Category'), choices=ArticleCategory.choices)
    content = models.BinaryField(_('Content'))
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)
