from django import forms

class userForm(forms.Form):
    num1 = forms.CharField(label="Value 1", required=False, widget=forms.TextInput(attrs={'class': "form-control"}) )
    num2 = forms.CharField(label="Value 2",widget=forms.TextInput(attrs={'class': "form-control"}))
    Shakib = forms.CharField(label="Value 3",widget=forms.TextInput(attrs={'class': "form-control"}))