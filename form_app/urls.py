from django.urls import path
from . import views

app_name = 'form_app'

urlpatterns = [
    path('', views.form_page, name='form_page'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('management/', views.management_system, name='management_system'),
    path('management/<str:section>/', views.management_system, name='management_system_section'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('toggle-status/<int:student_id>/', views.toggle_status, name='toggle_status'),
    path('edit/<int:student_id>/', views.edit_student, name='edit_student'),
    # path('mark-notifications-read/', views.mark_notifications_read, name='mark_notifications_read'),
    # path('mark-notifications-read/', views.mark_notifications_read, name='mark_notifications_read'),
]   