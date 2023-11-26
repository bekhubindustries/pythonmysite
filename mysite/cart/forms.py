from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        widget=forms.TextInput(attrs={'min': '1', 'value': '1'}),
        required=False,
    )
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
