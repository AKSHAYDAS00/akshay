from django.urls import path

from akshayapp import views

urlpatterns = [
    path('rocky/',views.home),
    path('major/',views.car),
    path('jinu/',views.sree),

    path('aa/',views.register,name='register'),
    path('emp/',views.emp,name='emp'),
    path('abc/',views.insert,name='new'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('pagination/',views.display),

]
