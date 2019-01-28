from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
DEFAULT_PRODUCT_TUPLES = [('a', 'art'), ('b', 'bracelet'), ('w', 'watch'), ('t', 'tech')]


class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(blank=False, max_length=100, default='')
    linenos = models.BooleanField(default=False)
    regular_price = models.DecimalField(blank=False, max_digits=8, decimal_places=2)
    listed_price = models.DecimalField(blank=False, max_digits=8, decimal_places=2)
    product_description = models.CharField(blank=True, default='', max_length=1500)
    product_type = models.CharField(blank=False, choices=DEFAULT_PRODUCT_TUPLES,max_length=100)
    is_stocked = models.BooleanField(default=True)
    is_flash_sale = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE)
    highlighted = models.TextField()
    # Will need to start many to one relationships to add additional fields
    # product_id = models.ForeignKey(auto_created=True, toPointToProductIdTable)
    # shipping_information_id = models.BigIntegerField(auto_created=True,
    #                                                  serialize=False,
    #                                                  verbose_name='ShippingId')

    class Meta:
        ordering = ('created',)
