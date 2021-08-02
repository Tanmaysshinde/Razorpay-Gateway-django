from django import forms
from .models import Forms

# class razForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     amount = forms.IntegerField()
class modelForm(forms.ModelForm):
    amount = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder' : 'Enter Amount'}), label='')
    class Meta:
        model = Forms
        fields = ['amount']