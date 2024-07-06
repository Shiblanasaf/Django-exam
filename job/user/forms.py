from typing import Any
from django import forms

# from django.core.exceptions import ValidationError

class JobForm(forms.Form):
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter name"}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter age"}))
    designation=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter pdesignation"}))
    phone=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter phone"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter email"}))