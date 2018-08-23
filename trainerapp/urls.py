from django.urls import path
from . import views

urlpatterns = [
    path('', views.upcoming_event_list, name='upcoming_event_list'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/inactive/', views.inactive_course_list, name='inactive_course_list'),
    path('events/past/', views.past_event_list, name='past_event_list'),
    path('students/', views.student_list, name='student_list'),
    path('students/inactive/', views.inactive_student_list, name='inactive_student_list'),
    path('student/add', views.StudentAdd.as_view(), name='student_add'),
    path('student/<int:pk>/detail/', views.StudentDetail.as_view(), name='student_detail'),
    path('student/<int:pk>/delete/', views.StudentDelete.as_view(), name='student_delete'),
    path('student/<int:pk>/edit/', views.StudentEdit.as_view(), name='student_edit'),
    path('event/<int:pk>/detail/', views.EventDetail.as_view(), name='event_detail'),
    path('event/add/', views.EventAdd.as_view(), name='event_add'),
    path('event/<int:pk>/edit/', views.EventEdit.as_view(), name='event_edit'),
    path('course/add', views.CourseAdd.as_view(), name='course_add'),
    path('course/<int:pk>/detail/', views.CourseDetail.as_view(), name='course_detail'),
    path('course/<int:pk>/edit/', views.CourseEdit.as_view(), name='course_edit'),
]