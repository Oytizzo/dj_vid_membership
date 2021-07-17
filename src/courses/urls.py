from django.urls import path

from . import views

urlpatterns = [
    # path('', views.courses, name='course-list'),
    path('', views.CourseListView.as_view(), name='course-list'),
    path('<slug>', views.CourseDetailView.as_view(), name='course-detail'),
]
