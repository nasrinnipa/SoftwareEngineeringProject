from django.forms import ModelForm
from .models import *

class Seller_Form(ModelForm):
    class Meta:
        model = Seller
        fields='__all__'
