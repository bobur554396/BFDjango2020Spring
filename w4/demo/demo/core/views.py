from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from demo.core.models import Author
from demo.core.serializers import AuthorSerializer


class AuthorListAPIView(mixins.ListModelMixin,
                        generics.GenericAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # permission_classes = ()
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (JSONWebTokenAuthentication,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
