from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применён по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors},
    )


from django.views import generic


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    context_object_name = 'book_list'  # ваше собственное имя переменной контекста в шаблоне
    queryset = Book.objects.all()
    template_name = 'catalog/book_list.html'  # Определение имени вашего шаблона и его расположения


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10
    context_object_name = 'author_list'
    queryset = Author.objects.all()
    template_name = 'catalog/author_list.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    book = Book
