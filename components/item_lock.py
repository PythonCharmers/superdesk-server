from models.item import ItemModel
# from models.base_model import ETAG
from superdesk import SuperdeskError
from superdesk.utc import utcnow


LOCK_USER = 'lock_user'
STATUS = '_status'


class ItemLock():
    def __init__(self, data_layer):
        self.data_layer = data_layer

    def lock(self, filter, user, etag):
        item_model = ItemModel(self.data_layer)
        item = item_model.find_one(filter)
        if item and self._can_lock(item, user):
            # filter[ETAG] = etag
            updates = {LOCK_USER: user, 'lock_time': utcnow()}
            item_model.update(filter, updates)
            item[LOCK_USER] = user
        else:
            raise SuperdeskError('Item locked by another user')
        return item

    def unlock(self, filter, user, etag):
        item_model = ItemModel(self.data_layer)
        filter[LOCK_USER] = user
        # filter[ETAG] = etag
        item = item_model.find_one(filter)
        if item:
            updates = {LOCK_USER: None, 'lock_time': None}
            item_model.update(filter, updates)

    def _can_lock(self, item, user):
        # TODO: implement
        return True
