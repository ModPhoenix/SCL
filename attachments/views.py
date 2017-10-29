import json
import os
import datetime

from imagekit import ImageSpec
from imagekit.processors import ResizeToFit
from django.http import JsonResponse
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import default_storage
from django.utils.translation import ugettext_lazy as _


class ImageOptimizer(ImageSpec):
    format = 'JPEG'
    options = {'quality': 99}

class ImageCrop(ImageSpec):
    processors = [
        ResizeToFit(width=687)
    ]

def image_upload(request):
    if request.FILES:
        the_file = request.FILES['image']
        allowed_types = ['image/jpeg', 'image/jpg', 'image/pjpeg', 'image/x-png', 'image/png', 'image/gif']
        if not the_file.content_type in allowed_types:
            return HttpResponse(json.dumps({'error': _('You can only upload images.')}),
                                content_type="application/json")
        # Other data on the request.FILES dictionary:
        # filesize = len(file['content'])
        # filetype = file['content-type']
        
        name = the_file.name
        now_date = datetime.date.today()
        upload_to = 'uploads/%d/%d/%d/' % (now_date.year, now_date.month, now_date.day)
        upload_crop = 'uploads/crop670/'
        image_generator = ImageOptimizer(source=the_file)
        result_generator = image_generator.generate()
        path = default_storage.save(os.path.join(upload_to, the_file.name), result_generator)
        image_crop = ImageCrop(source=result_generator)
        result_crop = image_crop.generate()
        path_crop = default_storage.save(os.path.join(upload_crop, the_file.name), result_crop)
        print(7)
        link = default_storage.url(path)
        link_crop = default_storage.url(path_crop)
        print()
        # return JsonResponse({'link': link})
        return HttpResponse(json.dumps({'link': link, 'name': name, 'link_crop': link_crop, }), content_type="application/json")