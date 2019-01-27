
from products.models import Product
from products.permissions import IsOwnerOrReadOnly
from products.serializers import ProductSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.reverse import reverse
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Dummy API')


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions
    """
    queryset = User.objects .all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    # noinspection PyUnresolvedReferences
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @action(detail=True,
            renderer_classes=[renderers.StaticHTMLRenderer],
            methods="GET")
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'products': reverse('snippet-list', request=request, format=format)
    })

