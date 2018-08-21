from django.urls import path
from . import views

urlpatterns = [
    path('', views.upcoming_event_list, name='upcoming_event_list'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/inactive/', views.inactive_course_list, name='inactive_course_list'),
    path('events/past/', views.past_event_list, name='past_event_list'),
    path('students/', views.student_list, name='student_list'),
    path('students/inactive', views.inactive_student_list, name='inactive_student_list'),
]