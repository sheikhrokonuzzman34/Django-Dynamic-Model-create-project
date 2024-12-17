from django.urls import path
from .views import *

urlpatterns = [
    
    path('create-table/', create_table_view, name='create_table'),
    path('<str:table_name>/add-row/', add_row_view, name='add_row'),
    path('<str:table_name>/list-rows/', list_rows_view, name='list_rows'),


    # for frontend developer
    path('count_info/', FileInfoCountAPIView.as_view(), name='file_count_info'), # count
    path('bar_chart/', FileInfoBarChartAPIView.as_view(), name='bar_chart'), # bra-chart 
    path('line_chart/', TagInfoLineChartAPIView.as_view(), name='line_chart'), # line-chart
    path('tag_relation/', TagRelationAPIView.as_view(), name='tag_relation'), # tag-relation
    path('file_percentage/', FileInfoPercentageAPIView.as_view(), name='file_dsshbord'), # file_percentage
    path('overall_analytics/',OverallAnalyticsAPIView.as_view(), name='overall_analytics'), # overall_analytics

   
]