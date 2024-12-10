from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    """
    Form class for users to get in touch directly with owner/admin
    """
    class Meta:
        model = Contact
        fields = '__all__'