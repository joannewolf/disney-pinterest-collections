from django import forms


class CreateAndUpdateBoardForm(forms.Form):
    name = forms.CharField(required=True, max_length=64)
    tag_ids = forms.CharField(required=False)
