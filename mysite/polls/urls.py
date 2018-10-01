from django.urls import path

from . import views

urlpatterns = \
    [
        path('<question_id>/name', views.hello_name),
        path('<int:question_id>/times2', views.times2),
        path('<int:num>/sums', views.sums),


    ]