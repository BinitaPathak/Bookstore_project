# from django.urls import path
#
# from categories.views import index, show, edit, create, search
#
# urlpatterns = [
#     path('categories', index, name='categories.index'),
#     path('categories/<int:pk>', show, name='categories.show'),
#     path('categories/<int:pk>/edit', edit, name='categories.edit'),
#     path('categories/create', create, name='categories.create'),
#     path('categories/search', search, name='categories.search'),
# ]

from django.urls import path

from categories.views import CategoriesListView, CategoryCreateView, CategoryDetailView, CategoryUpdateView

urlpatterns = [
    path('categories', CategoriesListView.as_view(), name='categories.index'),
    path('categories/<int:pk>', CategoryDetailView.as_view(), name='categories.show'),
    path('categories/<int:pk>/edit', CategoryUpdateView.as_view(), name='categories.edit'),
    path('categories/create', CategoryCreateView.as_view(), name='categories.create'),
]
