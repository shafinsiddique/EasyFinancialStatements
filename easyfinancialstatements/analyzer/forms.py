from django import forms

class CompanyForm(forms.Form):
    company_1 = forms.CharField(label="Company 1", max_length=100)
    company_2 = forms.CharField(label="Company 2", max_length=100)