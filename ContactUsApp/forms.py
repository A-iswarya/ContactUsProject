from django import forms
from .models import ContactUs

class ContactUsForm(forms.Form):
    Name = forms.CharField(max_length = 100,
                            widget = forms.TextInput(
                                            attrs = {
                                                'id' : 'inputName',
                                                'name' : 'Name',
                                                'class' : 'form-control',
                                                'placeholder' : 'Name',
                                                'pattern' : '^[a-zA-z][a-zA-Z\s]*$',
                                                'minlength' : '3'
                                                }
                            ))
    Email = forms.CharField(max_length=50,
                            widget = forms.TextInput(
                                            attrs = {
                                                'id' : 'inputEmail',
                                                'name' : 'Email',
                                                'class' : 'form-control',
                                                'placeholder' : 'Email address',
                                                 'required' : 'True',
                                                 # 'pattern' : "^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\.([a-zA-Z]{2,5})$"
                                            }
                            ))
    PhoneNumber = forms.CharField(max_length=10,
                            required=False,
                            widget = forms.TextInput(
                                            attrs = {
                                                'id' : 'inputNumber',
                                                'name' : 'PhoneNumber',
                                                'class' : 'form-control',
                                                'placeholder' : 'Phone Number',
                                                'pattern' : '[0-9]{10}'
                                            }
                            ))
    Description = forms.CharField(max_length=300,
                            widget = forms.Textarea(
                                            attrs = {
                                                'id' : 'inputDescription',
                                                'name' : 'Description',
                                                'class' : 'form-control',
                                                'placeholder' : 'Description',
                                                'rows' : '3',
                                                'minlength' : '20',
                                                'pattern' : '^[^\s]+.*$'
                                                 }
                            ))
