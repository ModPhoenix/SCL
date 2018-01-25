from dal import autocomplete
from .models import Guide


class GuideAdminForm(autocomplete.FutureModelForm):
    class Meta:
        model = Guide
        fields = ('__all__')
        widgets = {
            'tags': autocomplete.TaggitSelect2(
                'tag-autocomplete'
            )
        }
