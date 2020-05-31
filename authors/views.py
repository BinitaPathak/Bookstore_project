# from django.shortcuts import render
#
# from authors.models import Author
# from books.models import Book
#
# def index(request):
#     data = {
#         'title': 'authors Listing',
#         'object_list': Author.objects.all()
#     }
#
#     return render(request, 'authors/listing.html', data)
#
#
# def show(request, pk):
#     author = Author.objects.get(id=pk)
#     data = {
#         'title': 'Author Details',
#         'author': author.name,
#         'object': Book.objects.filter(author=author)
#     }
#
#     return render(request, 'authors/detail.html', data)
#
#
# def edit(request, pk):
#     data = {
#         'title': 'Edit Author',
#     }
#
#     return render(request, 'authors/update.html', data)
#
#
# def create(request):
#     data = {
#         'title': 'Create Author',
#     }
#
#     return render(request, 'authors/create.html', data)
#
#
# def search(request):
#     data = {
#         'title': 'Search authors',
#     }
#
#     return render(request, 'authors/listing.html', data)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from authors.models import Author
from books.models import Book


class AuthorsListView(ListView):
    model = Author
    template_name = 'authors/listing.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorsListView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Authors Listing'
        return context


class AuthorCreateView(LoginRequiredMixin, CreateView):
    login_url = '/auth/login'
    model = Author
    fields = ['name']
    template_name = 'authors/create.html'
    success_url = reverse_lazy('authors.index')


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(*args, **kwargs)
        context['author'] = context['object'].name
        context['object_list'] = Book.objects.filter(author=context['object'])
        context['title'] = 'Author Details'
        return context


class AuthorUpdateView(UpdateView):
    pass
