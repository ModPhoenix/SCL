from lxml import etree
from urllib import parse
import re

def get_image(html):
    '''
    Находит первое изображение
    и возвращает ссылку на него
    '''
    tree = etree.HTML(html)
    try:
        url = tree.xpath('//img/parent::a/@href')[0]
        img_url = url.split('/', 2)[2:][0]
        url_unicode = parse.unquote(img_url)
        upload = re.match(r'uploads', url_unicode)
        if upload:
            return url_unicode
    except:
        return None

def get_excerpt(html):
    ''' Возвращает первый параграф '''
    tree = etree.HTML(html)
    try:
        first_p = tree.xpath('//p[1]//text()')[0]
        return first_p
    except:
        return ''