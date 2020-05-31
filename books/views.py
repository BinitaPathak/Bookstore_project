# from django.shortcuts import render
#
# from books.models import Book
#
#
# def index(request):
#     data = {
#         'title': 'Books Listing',
#         'object_list': Book.objects.all(),
#     }
#
#     return render(request, 'books/listing.html', data)
#
#
# def show(request, pk):
#     data = {
#         'title': 'Book Details',
#         'object': Book.objects.get(id=pk)
#     }
#
#     return render(request, 'books/detail.html', data)
#
#
# def edit(request, pk):
#     data = {
#         'title': 'Edit Book',
#     }
#
#     return render(request, 'books/update.html', data)
#
#
# def create(request):
#     data = {
#         'title': 'Create Book',
#     }
#
#     return render(request, 'books/create.html', data)
#
#
# def search(request):
#     data = {
#         'title': 'Search Books',
#     }
#
#     return render(request, 'books/listing.html', data)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView

from books.forms import BookForm
from books.models import Book


class BooksListView(ListView):
    model = Book
    template_name = 'books/listing.html'
    queryset = Book.objects.filter().order_by('-title')

    def get_context_data(self, *args, **kwargs):
        context = super(BooksListView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Books Listing'
        return context


class BookCreateView(LoginRequiredMixin, CreateView):
    login_url = '/auth/login'
    form_class = BookForm
    template_name = 'books/create.html'
    success_url = reverse_lazy('books.index')

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        # form = HotelForm(request.POST, request.FILES)
        if request.method == 'POST':
            form = BookForm(request.POST, request.FILES)
            if form.is_valid():
                book_form = form.save()
                book_form.category.set(form.cleaned_data['category'])
                book_form.save()
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        else:
            return self.form_invalid(form)


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BookDetailView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Book Details'
        return context


class BookUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login'
    model = Book
    form_class = BookForm
    template_name = 'books/update.html'
    success_url = reverse_lazy('books.index')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


class BookDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/auth/login'
    model = Book
    success_url = reverse_lazy('books.index')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
