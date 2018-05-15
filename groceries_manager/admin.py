
from django.contrib import admin
from .models import Product_category, Product_group, Product_subgroup, Product, Supermarket, Ticket

# Register your models here.
class ProductInline(admin.TabularInline):
    model = Product
    extra = 3
    

class TicketAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['date']}),
        ('Date information',    {'fields': ['date'], 'classes': ['collapse']}),
    ]
    inlines = [ProductInline]
    # list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['date']
    search_fields = ['date']
    

admin.site.register(Ticket, TicketAdmin)