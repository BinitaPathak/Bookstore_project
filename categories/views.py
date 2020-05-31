# from django.shortcuts import render
#
# from categories.models import Category
#
#
# def index(request):
#     data = {
#         'title': 'categories Listing',
#         'object_list': Category.objects.all(),
#     }
#
#     return render(request, 'categories/listing.html', data)
#
#
# def show(request, pk):
#     data = {
#         'title': 'Category Details',
#         'object': Category.objects.get(id=pk)
#     }
#
#     return render(request, 'categories/detail.html', data)
#
#
# def edit(request, pk):
#     data = {
#         'title': 'Edit Category',
#     }
#
#     return render(request, 'categories/update.html', data)
#
#
# def create(request):
#     data = {
#         'title': 'Create Category',
#     }
#
#     return render(request, 'categories/create.html', data)
#
#
# def search(request):
#     data = {
#         'title': 'Search Categories',
#     }
#
#     return render(request, 'categories/listing.html', data)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from categories.models import Category


class CategoriesListView(ListView):
    model = Category
    template_name = 'categories/listing.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoriesListView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Categories Listing'
        return context


class CategoryCreateView(LoginRequiredMixin, CreateView):
    login_url = '/auth/login'
    model = Category
    fields = ['name']
    template_name = 'categories/create.html'
    success_url = reverse_lazy('categories.index')


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Category Details'
        return context


class CategoryUpdateView(UpdateView):
    pass
