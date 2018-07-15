from django import forms

class addingtocart(forms.Form):
    count = forms.IntegerField(widget = forms.TextInput(attrs={"class":"size8 m-text18 t-center num-product","value":"1","name":"num-product"}))
