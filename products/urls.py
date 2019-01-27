# from rest_framework import renderers
# from rest_framework.urlpatterns import format_suffix_patterns
# from products.views import SnippetViewSet, UserViewSet, api_root
# from django.urls import path
#
#
# snippet_list = SnippetViewSet.as_view(
#     {'get': 'list',
#      'post': 'create'}
# )
#
# snippet_detail = SnippetViewSet.as_view(
#     {'get': 'retrieve',
#      'put': 'update',
#      'patch': 'partial_update',
#      'delete': 'destroy'}
# )
#
# snippet_highlight = SnippetViewSet.as_view(
#     {'get': 'highlight'},
#     renderer_classes=[renderers.StaticHTMLRenderer])
#
# user_list = UserViewSet.as_view(
#     {'get': 'list'}
# )
#
# user_detail = UserViewSet.as_view(
#     {'get': 'retrieve'}
# )
#
#
# urlpatterns = format_suffix_patterns(
#     [path('', api_root),
#      path('products/', snippet_list, name='snippet-list'),
#      path('products/<int:pk>/', snippet_detail, name='snippet-detail'),
#      path('products/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#      path('users/', user_list, name='user-list'),
#      path('users/<int:pk>/', user_detail, name='user-detail')]
# )


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]