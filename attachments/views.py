import json
import os

from PIL import Image
from imagekit import ImageSpec
from imagekit.processors import ResizeToFill
from django.http import JsonResponse
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import default_storage
from django.utils.translation import ugettext_lazy as _


class ImageOptimizer(ImageSpec):
    #format = 'JPEG'
    options = {'quality': 99}

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
        img = Image.open(the_file)
        img_size = img.size
        upload_to = 'uploads/'
        image_generator = ImageOptimizer(source=the_file)
        result = image_generator.generate()
        path = default_storage.save(os.path.join(upload_to, the_file.name), result)
        print(7)
        link = default_storage.url(path)
        name = the_file.name.split('.')[0]
        width = img_size[0]
        height = img_size[1]
        print('width', width, 'height', height)
        # return JsonResponse({'link': link})
        return HttpResponse(json.dumps({'link': link, 'name': name, 'width': width, 'height': height}), content_type="application/json")