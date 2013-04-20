from django import template
from classytags.core import Tag, Options
from classytags.arguments import Argument
from zipdistance.models import ZipDistance

register = template.Library()

class Distance(Tag):
    options = Options(
        Argument('src', required=True, resolve=True),
        'to',
        Argument('dst', required=True, resolve=True),
        Argument('default', required=False, default="&mdash;", resolve=True)
    )

    def render_tag(self, context, src, dst, default):
        try:
            src_zip = ZipDistance.objects.get(zipcode=src)
            dst_zip = ZipDistance.objects.get(zipcode=dst)
        except ZipDistance.DoesNotExist:
            return default
        return src_zip.distance_between(dst_zip)

register.tag(Distance)
