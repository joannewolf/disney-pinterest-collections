from django import forms


class CreateAndUpdateArtistForm(forms.Form):
    name = forms.CharField(required=True, max_length=64)
    serial_number = forms.IntegerField(required=True)
    pinterest_page_url = forms.CharField(required=False)

    artstation_url = forms.CharField(required=False)
    behance_url = forms.CharField(required=False)
    deviantart_url = forms.CharField(required=False)
    facebook_url = forms.CharField(required=False)
    instagram_url = forms.CharField(required=False)
    pinterest_url = forms.CharField(required=False)
    pixiv_url = forms.CharField(required=False)
    tumblr_url = forms.CharField(required=False)
    twitter_url = forms.CharField(required=False)
    weibo_url = forms.CharField(required=False)
    other_url = forms.CharField(required=False)


class CreateAndUpdateBoardForm(forms.Form):
    name = forms.CharField(required=True, max_length=64)
    tag_ids = forms.CharField(required=False)
