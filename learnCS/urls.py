from django.urls import path
from . import views

urlpatterns = [
   
    # PATHS FOR NORMAL USE
    path(r'',views.homepage,name='homepage'),
    path(r'search/',views.search,name='search'),
    path(r'tutorials/<int:course_id>/',views.index, name='index'),
    path(r'lesson/<int:lesson_id>/',views.detail, name='detail'),
    path(r'exercises/<int:course_id>/',views.exercise, name='exercise'),
    path(r'problems/<int:lesson_id>/',views.problem, name='problem'),
    path(r'content/<int:exercise_id>/',views.content, name='content'),
    path(r'references/<int:course_id>/',views.reference, name='reference'),
    path(r'general/<int:course_id>/', views.general, name='general'),
    
    # PATH FOR ADMIN PAGES
    path(r'admindb/',views.admindb, name='admindb'),
    path(r'admindb/fulldb', views.fulldb, name='fulldb'),
    path(r'admindb/dbAdd', views.dbAdd, name='dbAdd'),
    path(r'admindb/dbDel-c/<int:course_id>/', views.dbDel_C, name='dbDel_C'),
    path(r'admindb/dbDel-l/<int:lesson_id>/', views.dbDel_L, name='dbDel_L'),
    path(r'admindb/dbDel-e/<int:exercise_id>/', views.dbDel_E, name='dbDel_E'),
    path(r'admindb/dbDel-r/<int:reference_id>/', views.dbDel_R, name='dbDel_R'),
]