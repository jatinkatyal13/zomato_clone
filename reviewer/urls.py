from django.urls import path

from reviewer import views

urlpatterns = [
  path('', views.Index.as_view(), name = 'index'),
  path('restaurant/<int:pk>', views.Restaurant.as_view(), name = 'restaurant'),
  path('restaurant/<int:pk>/add_review', views.AddReview.as_view(), name = 'restaurant_review'),
]
