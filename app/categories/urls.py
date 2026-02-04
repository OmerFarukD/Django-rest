from django.urls import path

from .views import CategoryListAV, CategoryDetilsAV

urlpatterns = [
    path('', CategoryListAV().as_view(), name="categories"),
    path('<int:id>', CategoryDetilsAV().as_view(), name="category detail")
]