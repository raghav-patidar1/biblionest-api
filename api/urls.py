from django.urls import path

from . import views

urlpatterns = [
    path('library-data/', views.LibraryBranchListAPIView.as_view())
]