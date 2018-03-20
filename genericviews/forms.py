from django import forms


class ProductForm(forms.Form):
    title = forms.CharField(label='Title', max_length=255, required=True,
                            widget=forms.TextInput(attrs={
                                'class': 'form-control container spacebelow',
                            }))

    description = forms.CharField(label='Description', max_length=255, required=True,
                                  widget=forms.Textarea(attrs={
                                      'class': 'form-control container spacebelow',
                                  }))
