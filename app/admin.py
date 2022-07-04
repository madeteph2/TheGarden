from django.contrib import admin
from .models import Marca, Producto, Contacto
from .forms import ProductoForm

# Register your models here.

#AGREGAR COLUMNAS EN ADMIN/PRODUCTOS
class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","cantidad","disponible","marca"]

#EDITAR PRODUCTOS EN LA MISMA COLUMNA
    list_editable =["precio", "cantidad"]

#BUSQUEDA POR CAMPO
    search_fields = ["nombre"]

#AGREGAR FILTRO PARA BUSQUEDA
    list_filter = ["disponible", "marca"]

#DECLARAR CUANTOS PRODUCTOS SE MUESTRAN EN LA PAGINA /ADMIN/PRODUCTOS
    list_per_page = 25

#AGREGAR VALIDACIONES A LA PAGINA DE ADMIN DESDE /FORMS.PY
    form = ProductoForm

admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)

