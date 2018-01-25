from django import forms
from dal import autocomplete
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control hide'}),
            'published': forms.CheckboxInput(attrs={'class': 'custom-control-input'}),
        }


class PostAdminForm(autocomplete.FutureModelForm):
    class Meta:
        model = Post
        fields = ('__all__')
        widgets = {
            'tags': autocomplete.TaggitSelect2(
                'tag-autocomplete'
            )
        }