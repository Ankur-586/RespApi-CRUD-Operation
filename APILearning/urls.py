from django.urls import path
from . import views

urlpatterns = [
    path('',views.moduleapi.as_view()),
    path('<pk>/',views.moduleapiDetail.as_view())
]