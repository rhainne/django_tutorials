
from django.contrib import admin
from .models import Product_category, Product_group, Product_subgroup, Product, Supermarket, Ticket, Ticket_line

# Register your models here.
class Ticket_lineInline(admin.TabularInline):
    model = Ticket_line
    extra = 3
    

class TicketAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Ticket information',    {'fields': ['date', 'id_supermarket']}),
    ]
    inlines = [Ticket_lineInline]
    list_display = ('id', 'id_supermarket', 'date')
    list_filter = ['date']
    search_fields = ['date']
    

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Product)
admin.site.register(Supermarket)
admin.site.register(Product_category)
admin.site.register(Product_group)
admin.site.register(Product_subgroup)
