from django.contrib import admin
from .models import Category, Product, Commande

# Register your models here.
admin.site.site_header = "Site de E-Commerce || Toto-Shop"
admin.site.site_title = "Toto-Shop"
admin.site.index_title = "Manageur"

class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_added')
    
class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added') # Afficher les elements ces details sous forme de tableau
    search_fields = ('title',)   # Rechercher par rapport a
    list_editable = ('price',)   # Les champs editables directement
    
class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'nom', 'email', 'address', 'ville', 'pays', 'total', 'date_commande')

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Commande, AdminCommande)
