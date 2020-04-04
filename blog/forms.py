from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=128)
    content = forms.CharField(widget=forms.Textarea())


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea())
    post = forms.IntegerField(widget=forms.HiddenInput())
