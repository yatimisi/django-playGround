from django import forms


class BmiForm(forms.Form):
    heigh = forms.FloatField(min_value=1, label='身高')
    kg = forms.FloatField(min_value=1, label='體重')