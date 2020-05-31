# from django.urls import path
#
# from books.views import index, show, edit, create, search
#
# urlpatterns = [
#     path('books', index, name='books.index'),
#     path('books/<int:pk>', show, name='books.show'),
#     path('books/<int:pk>/edit', edit, name='books.edit'),
#     path('books/create', create, name='books.create'),
#     path('books/search', search, name='books.search'),
# ]
from django.urls import path
from django.views.generic import TemplateView

from books.views import BooksListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books', BooksListView.as_view(), name='books.index'),
    path('books/<int:pk>', BookDetailView.as_view(), name='books.show'),
    path('books/<int:pk>/edit', BookUpdateView.as_view(), name='books.edit'),
    path('books/<int:pk>/delete', BookDeleteView.as_view(), name='books.delete'),
    path('books/create', BookCreateView.as_view(), name='books.create'),
    path('user-login/', TemplateView.as_view(template_name="UserLogin.html"), name="user_login"),
    path('seller-login/', TemplateView.as_view(template_name="SellerLogin.html"), name="seller_login"),
    path('contact/', TemplateView.as_view(template_name="ContactPage.html"), name="contact"),
]
