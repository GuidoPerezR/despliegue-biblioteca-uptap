from django.urls import path
from .views import booksPage, bookDetail, bookRequest, adminView, adminBookDetail, adminDeleteBook, adminAddBook, adminRequestList, LogInUser
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login

app_name='modulo'
urlpatterns = [
    path('', views.home, name='home'),
    path('BooksPage', views.booksPage, name='BooksPage'),
    # path('BookDetail/<id>',bookDetail, name='BookDetail'),
    # path('BookRequest/<id>', bookRequest, name='BookRequest'),
    path('AdminBooksPage/', views.adminView, name='AdminBooksPage'),
    # path('AdminBookDetail/<id>/', adminBookDetail, name='AdminBookDetail'),
    # path('AdminDeleteBook/<id>/',adminDeleteBook, name='AdminDeleteBook'),
    # path('AdminAddBook/', adminAddBook, name='AdminAddBook'),
    # path('AdminRequestList/', adminRequestList, name='AdminRequestList'),
] 