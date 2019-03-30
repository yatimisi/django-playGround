from django import forms


class BmiForm(forms.Form):
    heigh = forms.FloatField(min_value=1, label='身高')
    kg = forms.FloatField(min_value=1, label='體重')


class DeleteConfirmForm(forms.Form):
    check = forms.BooleanField(label='你確定要刪除嗎？')
