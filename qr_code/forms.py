from django import forms


class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(
        label="Name",
        max_length=50, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter name'}))
    url = forms.URLField(
        label="URL", 
        max_length=200,
        widget=forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter URL'}))