from django import forms


class MeliCredentialForm(forms.Form):
    prefix = "meli"
    enable = forms.BooleanField(required=False)
    store_id = forms.CharField(max_length=100, required=False)


class B2WCredentialForm(forms.Form):
    prefix = "b2w"
    enable = forms.BooleanField(required=False)
    client_id = forms.CharField(max_length=100, required=False)
