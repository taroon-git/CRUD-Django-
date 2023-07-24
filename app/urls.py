from django.urls import path,include

from . import views
urlpatterns = [
    # path('',views.InsertView, name='Insertview'),

    path('insert/',views.InsertView, name = 'Insert'),
    path('show/',views.ShowPage,name='showpage'),
    path('edit/<int:pk>',views.EditPage, name='editpage'),
    path('update/<int:pk>',views.UpdateView, name='update'),
    path('delete/<int:pk>',views.DeleteView, name='delete')

]
