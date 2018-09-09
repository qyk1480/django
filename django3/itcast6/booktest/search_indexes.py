from haystack import indexes
from booktest.models import Tinymce1


class Tinymce1Index(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Tinymce1

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
