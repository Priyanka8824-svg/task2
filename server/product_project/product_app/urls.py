from django.urls import path
from .views import *

urlpatterns = [
    path('product/create/', create_product ),
    path('product/list/', list_product ),
    path('product/update/<pk>/', update_product ),
    path('product/delete/<pk>/', delete_product ),
    path('product/retrieve/<pk>/', retrieve_product),

    path('demo/',demo)
]


