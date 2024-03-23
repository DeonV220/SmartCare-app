from django.urls import path
from . import views

urlpatterns = [
    path('patient/signup/', views.patient_signup, name='patient_signup'),
    path('patient/login/', views.patient_login, name='patient_login'),
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),

    path('login/', views.login, name='login'),
    
    path('doctor/signup/', views.doctor_signup, name='doctor_signup'),
    path('doctor/login/', views.doctor_login, name='doctor_login'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('logout/', views.logout_view, name='logout'),

    path('update/user/<int:user_id>/', views.update_user, name='update_user'),
    path('delete/user/<int:user_id>/', views.delete_user, name='delete_user'),
]






# from django.urls import path
# from . import views

# urlpatterns = [
#     path('signup/', views.signup, name='signup'),
#     path('login/', views.login, name='login'),
#     path('logout/', views.logout_view, name='logout'),
#     path('dashboard/doctor/', views.doctor_dashboard, name='doctor_dashboard'),
#     path('dashboard/nurse/', views.nurse_dashboard, name='nurse_dashboard'),
#     path('dashboard/patient/', views.patient_dashboard, name='patient_dashboard'),
#     path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
#     path('user/update/<int:user_id>/', views.update_user, name='update_user'),
#     path('user/delete/<int:user_id>/', views.delete_user, name='delete_user'),
# ]