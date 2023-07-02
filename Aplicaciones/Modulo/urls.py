from django.urls import path
from .views import booksPage, bookDetail, bookRequest, adminView, adminBookDetail, adminDeleteBook, adminAddBook, adminRequestList, LogInUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login

app_name='modulo'
urlpatterns = [
    path('', LogInUser, name = 'login'),
    path('booksPage', booksPage, name='BooksPage'),
    path('Logout/', logout_then_login, name='logout'),
    path('BookDetail/<id>',bookDetail, name='BookDetail'),
    path('BookRequest/<id>', bookRequest, name='BookRequest'),
    path('AdminBooksPage/', login_required(adminView), name='AdminBooksPage'),
    path('AdminBookDetail/<id>/', adminBookDetail, name='AdminBookDetail'),
    path('AdminDeleteBook/<id>/',adminDeleteBook, name='AdminDeleteBook'),
    path('AdminAddBook/', adminAddBook, name='AdminAddBook'),
    path('AdminRequestList/', adminRequestList, name='AdminRequestList'),
] 