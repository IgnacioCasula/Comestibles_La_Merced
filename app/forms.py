from django import forms
from .models import elproducto

class elproductoForm(forms.ModelForm):
    class Meta:
        model = elproducto
        fields = ['nombre', 'precio', 'stock']


from .models import producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields ='__all__'