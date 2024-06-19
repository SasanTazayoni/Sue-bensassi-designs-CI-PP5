from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=50, required=True)
    enquiry = forms.CharField(widget=forms.Textarea, max_length=1000, required=True)
