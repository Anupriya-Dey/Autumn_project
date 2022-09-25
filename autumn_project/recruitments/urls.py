from django.urls import path
from recruitments import views

urlpatterns = [
    path('recruitments/', views.recruitments_list),
    path('recruitments/<int:pk>/', views.recruitments_detail),
]