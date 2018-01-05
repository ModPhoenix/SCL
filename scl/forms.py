from django import forms

from .models import User

class PublicProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'biography',
                  'location', 'handle',
                  'organization', ]