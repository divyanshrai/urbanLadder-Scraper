from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

from util.choices import MEASUREMENT_TYPE, ATTRIBUTE_TYPE
import uuid

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null = True)
    ref_image = models.ImageField(upload_to="%Y/%m/%d", blank=True)
    active = models.BooleanField(default=True)
  
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model): 
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, help_text="A small description of the product")
    link = models.URLField(null=True, blank=True, max_length=1000)
    active = models.BooleanField(default=True)

    price = models.DecimalField(decimal_places=2, max_digits=10)
    discounted_price = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    delivery_fee = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category', null=True, blank=True)
    tags = models.ManyToManyField(Tag, help_text="Relative tags for the product", blank=True)

    related_products = models.ManyToManyField("self", help_text="Related products", blank=True)

    ref_image = models.ImageField(upload_to="%Y/%m/%d", blank=True, help_text="An image that best shows the product")
    size = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name + " - " + str(self.u_id)
   
    def imgsrc_html(self, width=150, height=150):
        if height==None: hstr = ''
        else: hstr = 'height="{}"'.format(height)
        return mark_safe('<img src="{}" width={} {}/>'.format(self.ref_image.url if self.ref_image else None, width, hstr))

# class ProductExtraImage():
#     product = models.ForeignKey("ScrapeProducts.Product", on_delete=models.CASCADE, null=True, blank=True)
#     image = models.ImageField(upload_to="%Y/%m/%d", blank=True, help_text="Alternative images for the product")

#     def imgsrc_html(self, width=75, height=75):
#         hstr = 'height="{}"'.format(height)
#         return mark_safe('<img src="{}" width={} {}/>'.format(self.image.url, width, hstr))
