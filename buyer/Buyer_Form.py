from django.forms import ModelForm
from .models import *

class Buyer_Form(ModelForm):
    class Meta:
        model = Buyer
        fields='__all__'
