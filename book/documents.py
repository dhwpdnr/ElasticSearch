from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer as es_analyzer

from .models import *

INDEX = Index("books")
INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)
html_strip = es_analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


@INDEX.doc_type
class BookDocument(Document):
    """Book Elasticsearch document."""
    title = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.KeywordField(),
        }
    )

    class Django(object):
        """Inner nested class Django."""

        model = Book
        fields = [
            "id",
            "description",
            "summary",
            "state",
            "price",
            "pages",
        ]

        # Add the mapping for the title field
