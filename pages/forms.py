from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
  email = forms.EmailField(label='Email :', widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control ', 'required': 'True'}))
  name = forms.CharField(label='Name :', widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control ', 'required': 'True'}))
  message = forms.CharField(label='Message :', widget=forms.Textarea(attrs={'placeholder': 'What you want to say? Are You have a project? or you need help?', 'class': 'form-control ', 'required': 'True'}))
  class Meta:
    model = Contact
    fields = ['name', 'email', 'message']

  def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        return email