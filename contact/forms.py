from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    company = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 100}))