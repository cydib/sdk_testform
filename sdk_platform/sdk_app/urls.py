from django.urls import path
from sdk_app import views

urlpatterns = [
    path('sdk_manage/', views.sdk_manage),
    path('sdk_test/', views.sdk_test),

]