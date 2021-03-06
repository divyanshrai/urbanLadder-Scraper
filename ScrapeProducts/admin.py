from django.contrib import admin

# Register your models here.
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'active']
    search_fields = ['name', 'description']
    list_filter = ['active']

admin.site.register(Category,CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Tag, TagAdmin)

class ProductAdmin(admin.ModelAdmin):
    def display_of_image(self, p_obj):
        p_img_html_str = p_obj.imgsrc_html(height=150, width=150)
        return mark_safe(p_img_html_str)
    
    def display_of_small_image(self, p_obj):
        p_img_html_str = p_obj.imgsrc_html(width=75, height=75)
        print(p_img_html_str)
        return mark_safe(p_img_html_str)
    
    def short_html_description(self, p_obj):
        return mark_safe(p_obj.description[:50])

    def short_link(self, p_obj):
        return p_obj.link[:15] if p_obj.link else None  
    
    def related_products(self, obj):
        return "\n".join([p.name for p in obj.related_products.all()])

    def all_tags(self, obj):
        return "\n".join([p.tname for p in obj.tags.all()])


    list_display = ['pk', 'display_of_small_image', 'name', 'short_html_description', 'category',
            'price', 'discounted_price', 'delivery_fee', 'related_products',
            'all_tags', 'short_link', 'size']
    search_fields = ['name', 'description']
    list_filter = ['active', 'tags', 'category']
    autocomplete_fields  = ['tags']
    filter_horizontal=['related_products']
    fieldsets = (
            ('General product info', {
                'fields' : [('name', 'category'),
                ('link'),
                ('related_products', 'tags')]
                }),
            ("Visualization and dimensions", {
                'fields' : ('display_of_image', 'ref_image'),
                }),
            ("Pricing", {
                'fields' : ('price', 'discounted_price', 'delivery_fee'),
                }),
            ("HTML inputs for Product", {
                'fields' : ('description', 'size'),
                }),
            
        )

#    inlines = [ProductExtraImageInlineAdmin]

    readonly_fields = (
            'display_of_image',
        )
    

admin.site.register(Product, ProductAdmin)