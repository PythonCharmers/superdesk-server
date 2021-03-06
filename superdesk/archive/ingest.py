from superdesk.base_model import BaseModel
from .common import base_schema, extra_response_fields, item_url, facets
from .common import on_create_item, on_create_media_archive, on_update_media_archive, on_delete_media_archive


class IngestModel(BaseModel):
    endpoint_name = 'ingest'
    schema = {
        'archived': {
            'type': 'datetime'
        }
    }
    schema.update(base_schema)
    extra_response_fields = extra_response_fields
    item_url = item_url
    datasource = {
        'backend': 'elastic',
        'facets': facets
    }

    def on_create(self, docs):
        on_create_item(docs)
        on_create_media_archive()

    def on_update(self, updates, original):
        on_update_media_archive()

    def on_delete(self, doc):
        on_delete_media_archive()
