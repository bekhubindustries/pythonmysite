from django.urls import path
from . import views
from .views import Search

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about),
    path('item/<int:item_id>', views.detail, name='detail'),
    path('just/', views.just, name='just'),
    path('men/', views.index_men, name='men'),
    path('men/item/<int:item_id>', views.detail, name='item_detail'),
    path('women/', views.index_women, name='women'),
    path('women/item/<int:item_id>', views.detail, name='item_detail'),
    path('PERFUMES_AND_BODY_SKIN_CARE_PRODUCTS/', views.index_PERFUMES_AND_BODY_SKIN_CARE_PRODUCTS, name='PERFUMES_AND_BODY_SKIN_CARE_PRODUCTS'),
    path('PERFUMES_AND_BODY_SKIN_CARE_PRODUCTS/item/<int:item_id>/', views.detail, name='item_detail'),
    path('search/',Search.as_view(),name='search'),
    path('search/item/<int:item_id>/',views.detail,name='item_detail'),

]
