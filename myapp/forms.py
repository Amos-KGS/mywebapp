from django import forms
from crispy_forms.helper import FormHelper

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name'}), max_length=200, required=True)
    from_email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your Email Address'}),required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email Subject'}),max_length=500, required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type your message here'}), max_length=1000)
    

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = False
        self.fields['from_email'].label = False
        self.fields['subject'].label = False
        self.fields['message'].label = False