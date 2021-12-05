from django import forms


class NovelForm(forms.Form):
    author_name = forms.CharField(required=False, max_length=64, label="作家名")
    keyword = forms.CharField(required=False, max_length=64, label="キーワード")
