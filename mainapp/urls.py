from django.urls import path
from .views import *

urlpatterns = [
    
    path('create-table/', create_table_view, name='create_table'),
    path('<str:table_name>/add-row/', add_row_view, name='add_row'),
    path('<str:table_name>/list-rows/', list_rows_view, name='list_rows'),
   
]