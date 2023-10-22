from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about),
    path('item/<int:item_id>', views.detail, name='detail')
]
