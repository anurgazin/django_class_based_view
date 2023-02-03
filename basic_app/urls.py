from django.urls import path

from basic_app import views

app_name = "basic_app"

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name='delete'),
    path('student/create/<int:fk>', views.StudentCreateView.as_view(), name='add_student'),
    path('student/update/<int:pk>/', views.StudentUpdateView.as_view(), name='update_student'),
    path('student/delete/<int:pk>/', views.StudentDeleteView.as_view(), name='delete_student'),
]
