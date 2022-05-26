from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('signup', views.UserAPI.as_view(), name='user-list'),
    path('user_details/<int:pk>', views.UserDetails.as_view(), name='user_details'),
    path('register', views.UserDetails.as_view(), name='create_user')

]
