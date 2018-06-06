import json
import os
import datetime

from PIL import Image
from imagekit import ImageSpec
from imagekit.processors import ResizeToFit
from django.http import JsonResponse
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import default_storage
from django.utils.translation import ugettext_lazy as _


class ImageCrop(ImageSpec):
    processors = [ResizeToFit(width=780)]
    options = {'quality': 95}

def image_upload(request):
    if request.FILES:
        the_file = request.FILES['image']
        allowed_types = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif']
        if not the_file.content_type in allowed_types:
            return HttpResponse(json.dumps({'error': _('You can only upload images.')}),
                                content_type="application/json")
        # Other data on the request.FILES dictionary:
        # filesize = len(file['content'])
        # filetype = file['content-type']
        
        name = the_file.name
        im = Image.open(the_file)
        (width, height) = im.size
        print(width, height)
        now_date = datetime.date.today()
        upload_to = 'uploads/%d/%d/%d/' % (now_date.year, now_date.month, now_date.day)
        path = default_storage.save(os.path.join(upload_to, the_file.name), the_file)
        link = default_storage.url(path)
        link_crop = None
        if width > 800:
            upload_crop = 'uploads/%d/%d/%d/crop800/' % (now_date.year, now_date.month, now_date.day)
            image_crop = ImageCrop(source=the_file)
            result_crop = image_crop.generate()
            path_crop = default_storage.save(os.path.join(upload_crop, the_file.name), result_crop)
            link_crop = default_storage.url(path_crop)

        print(HttpResponse(json.dumps({'link': link, 'name': name, 'link_crop': link_crop, }), content_type="application/json"))
        
        return HttpResponse(json.dumps({'link': link, 'name': name, 'link_crop': link_crop, }), content_type="application/json")