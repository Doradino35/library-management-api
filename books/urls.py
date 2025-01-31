from django.urls import path
from . import views

urlpatterns = [
    
    path('books/', views.BookListCreateView.as_view(), name='book-list-create'),

    path('books/<uuid:pk>/', views.BookDetailView.as_view(), name='book-detail'),
]