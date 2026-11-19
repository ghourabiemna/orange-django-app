from django import forms
from .models import Interface

class InterfaceForm(forms.ModelForm):
    class Meta:
        model = Interface
        fields = ['interface_name', 'description','ne_name', 'ipv4_address', 'subnet_mask','mac_address','rate', 'admin_status', 'ipv4_status']
