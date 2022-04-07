from django import forms

class ClientForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    second_name = forms.CharField(max_length=20)
    order_name = forms.CharField(max_length=50)
    total = forms.IntegerField(min_value=0)