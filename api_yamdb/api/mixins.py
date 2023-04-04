from rest_framework.mixins import (CreateModelMixin,
                                   ListModelMixin, DestroyModelMixin)
from rest_framework.viewsets import GenericViewSet


class ListCreatemixin(GenericViewSet, CreateModelMixin,
                      ListModelMixin, DestroyModelMixin):
    pass
