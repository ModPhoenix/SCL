from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType

from .models import Comment
from .forms import CommentForm


def add_comment(request):
    
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        c_type = comment_form.cleaned_data['content_type']
        content_type = ContentType.objects.get(model=c_type)
        object_id = comment_form.cleaned_data['object_id']
        comment_data = comment_form.cleaned_data['comment']
        parent_object = None

        try:
            parent_id = comment_form.cleaned_data['parent_id']
        except:
            parent_id = None

        if parent_id is not None:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists():
                parent_object = parent_qs.first()

        new_comment = Comment.objects.create(
            user=request.user,
            content_type=content_type,
            object_id=object_id,
            comment=comment_data,
            parent=parent_object,
        )
        
        return HttpResponseRedirect("%s#comment-%s" % (new_comment.content_object.get_absolute_url(), new_comment.id))
