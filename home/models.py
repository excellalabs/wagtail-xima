from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

class InventoryItem(Page, models.Model):
    cost = models.DecimalField(decimal_places=2, max_digits=5)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    item_number = models.IntegerField(blank=True, null=True)
    SKU = models.TextField(blank=True, null=True, max_length=8)
    description = models.TextField(default="Please include a description of the product")
    stocked_quantity = models.IntegerField(default=0)
    pic = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = Page.content_panels + [
        FieldPanel('cost'),
        FieldPanel('price'),
        FieldPanel('description'),
        FieldPanel('item_number'),
        FieldPanel('SKU'),
        ImageChooserPanel('pic'),
    ]

    search_fields = Page.search_fields + (
        index.SearchField('description'),
    )
