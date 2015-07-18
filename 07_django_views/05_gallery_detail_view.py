from django.views.generic import DetailView

from cms.models import Gallery


class GalleryDetail(DetailView):
    model = Gallery

    def get_template_names(self):
        if self.object.layout == 'HORI':
            return (
                'cms/gallery_detail_horizontal.html',
            )
        elif self.object.layout == 'VERT':
            return (
                'cms/gallery_detail_vertical.html',
            )
        else:
            return (
                'cms/gallery_detail_links.html',
            )
