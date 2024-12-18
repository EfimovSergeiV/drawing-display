from draw.models import FileModel


from django_opensearch_dsl import Document
from django_opensearch_dsl.registries import registry
from django_opensearch_dsl.fields import GeoPointField


@registry.register_document
class FileDocument(Document):
    """ OpenSearch """

    class Index:
        name = 'files'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }
        auto_refresh = True


    class Django:
        model = FileModel
        fields = [
            'id',
            'name',
            'link',
        ]