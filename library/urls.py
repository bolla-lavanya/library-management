from django.urls import path
from . import views
urlpatterns=[
    path('',views.display),
    path('insert/',views.insertBook,name="inserturl"),
    path('update/<int:lno>/',views.updateBook,name="updateurl"),
    path('delete/<int:eno>/',views.deleteBook,name='deleteurl'),
    path('select/',views.selectBook,name='selecturl'),
]