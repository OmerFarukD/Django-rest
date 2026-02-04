from django.urls import path

from .views import CommentListByProductView, CommentDetailsView, CommentDeleteView

urlpatterns = [
    path('<int:id>', CommentDetailsView.as_view(), name='comments_by_id'),
    path('<int:id>/product',CommentListByProductView().as_view(),name='comments_by_product'),
    path('<int:id>/product',CommentDeleteView().as_view(),name='delete_by_comments')
]


