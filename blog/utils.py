from lxml import etree
from urllib import parse

def get_image(content):
    tree = etree.HTML(content)
    try:
        url = tree.xpath('//img/parent::a/@href')[0]
        img_url = url.split('/', 2)[2:][0]
        url_unicode = parse.unquote(img_url)
        return url_unicode
    except:
        return None