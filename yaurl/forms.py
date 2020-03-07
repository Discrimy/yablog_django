from django import forms


class ShortedUrlForm(forms.Form):
    original_url = forms.URLField(label='Original URL', max_length=200)
