from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from .forms import AttachmentForm
from .models import Attachment

class BasicUploadView(View):
    def get(self, request):
        attachments_list = Attachment.objects.all()
        return render(self.request, 'photos/basic_upload/index.html', {'attachments': attachments_list})

    def post(self, request):
        form = AttachmentForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            attachment = form.save()
            data = {'is_valid': True, 'name': attachment.file.name, 'url': attachment.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)