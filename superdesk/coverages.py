from superdesk.base_model import BaseModel
from superdesk.notification import push_notification


def init_app(app):
    CoverageModel(app=app)


def rel(resource, embeddable=False):
    return {
        'type': 'objectid',
        'data_relation': {'resource': resource, 'field': '_id', 'embeddable': embeddable}
    }


class CoverageModel(BaseModel):
    endpoint_name = 'coverages'
    schema = {
        'headline': {'type': 'string'},
        'coverage_type': {
            'type': 'string',
            'allowed': ['story', 'photo', 'video', 'graphics', 'live-blogging'],
            'default': 'story',
            'required': 'true'
        },
        'ed_note': {'type': 'string'},
        'scheduled': {'type': 'datetime'},
        'delivery': {'type': 'string'},
        'assigned_user': rel('users', True),
        'assigned_desk': rel('desks', True),
        'planning_item': {'type': 'string'},
    }

    def on_create_coverage(self, docs):
        push_notification('coverages', created=1)

    def on_update_coverage(self, updates, original):
        push_notification('coverages', updated=1)

    def on_delete_coverage(self, doc):
        push_notification('coverages', deleted=1)
