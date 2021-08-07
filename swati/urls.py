from django.urls import path


from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add',views.add,name='add'),
    path('index',views.index,name='index'),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
    path('remove/<int:id>',views.remove,name="remove"),
]