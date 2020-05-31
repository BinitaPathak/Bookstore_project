# from django.urls import path
#
# from authors.views import index, show, edit, create, search
#
# urlpatterns = [
#     path('authors', index, name='authors.index'),
#     path('authors/<int:pk>', show, name='authors.show'),
#     path('authors/<int:pk>/edit', edit, name='authors.edit'),
#     path('authors/create', create, name='authors.create'),
#     path('authors/search', search, name='authors.search'),
# ]

from django.urls import path

from authors.views import AuthorsListView, AuthorCreateView, AuthorDetailView, AuthorUpdateView

urlpatterns = [
    path('authors', AuthorsListView.as_view(), name='authors.index'),
    path('authors/<int:pk>', AuthorDetailView.as_view(), name='authors.show'),
    path('authors/<int:pk>/edit', AuthorUpdateView.as_view(), name='authors.edit'),
    path('authors/create', AuthorCreateView.as_view(), name='authors.create'),
]
