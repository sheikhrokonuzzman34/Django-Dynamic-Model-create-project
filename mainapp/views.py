from django.shortcuts import render, redirect
from django.apps import apps
from django.http import JsonResponse
from .dynamic_model_creator import create_dynamic_table
from django.contrib.auth.decorators import login_required
from django.db import models
from rest_framework.response import Response
from rest_framework.views import APIView


@login_required
def create_table_view(request):
    """
    Create a dynamic table based on user input.
    """
    if request.method == 'POST':
        table_name = request.POST['table_name']
        fields = {
            'name': models.CharField(max_length=100),  # Example field
            'age': models.IntegerField(),             # Example field
        }
        create_dynamic_table(table_name, fields)
        return JsonResponse({'success': f"Table '{table_name}' created successfully!"})
    return render(request, 'create_table.html')

@login_required
def add_row_view(request, table_name):
    """
    Add a row to a dynamically created table.
    """
    if request.method == 'POST':
        # Get the dynamic model
        DynamicModel = apps.get_model('mainapp', table_name.capitalize())

        # Create a new row with the submitted data and associate it with the current user
        new_row = DynamicModel.objects.create(
            name=request.POST['name'],  # Example field
            age=request.POST['age'],    # Example field
            created_by=request.user     # Set the creator of the row
        )
        return JsonResponse({'success': f"Row added to {table_name}!"})
    return render(request, 'add_row.html', {'table_name': table_name})

@login_required
def list_rows_view(request, table_name):
    """
    List rows from a dynamically created table, filtered by the current user.
    """
    # Get the dynamic model
    DynamicModel = apps.get_model('mainapp', table_name.capitalize())

    # Filter rows based on the current user
    rows = DynamicModel.objects.filter(created_by=request.user)
    return render(request, 'list_rows.html', {'rows': rows, 'table_name': table_name})




# file info count
class FileInfoCountAPIView(APIView):
    def get(self, request, format=None):
        data = {
            "documents": 30,
            "tags": 21,
            "workflow": 25,
            "tag_relations": 28,
        }
        return Response(data)
 

class FileInfoBarChartAPIView(APIView):
    def get(self, request, format=None):
        data = {
        "file_count": [
                    {"file_type": "pdf", "count": 14},
                    {"file_type": "docx", "count": 8},
                    {"file_type": "xlsx", "count": 6},
                    {"file_type": "png", "count": 13},
                    {"file_type": "jpg", "count": 11},
                    {"file_type": "zip", "count": 7},
                    {"file_type": "txt", "count": 10}
      ]
        }
        return Response(data)
    

class TagInfoLineChartAPIView(APIView):
    def get(self, request, format=None):
        data = {
            "tag_counts": [
                        {"tag": "important", "count": 5},
                        {"tag": "confidential", "count": 3},
                        {"tag": "archive", "count": 4},
                        {"tag": "review", "count": 2},
                        {"tag": "shared", "count": 3},
                        {"tag": "urgent", "count": 6},
                        {"tag": "public", "count": 2}
  ]
        }
        return Response(data)
 

class TagRelationAPIView(APIView):
    def get(self, request, format=None):
        data = {
            "equipment": 192,
            "instruments": 5000,
            "pipelines": 32,
        }
        return Response(data)
 

class FileInfoPercentageAPIView(APIView):
    def get(self, request, format=None):
        data = {
            "file": [
    {"file_type": "pdf", "percentage": 11.54},
    {"file_type": "docx", "percentage": 16.67},
    {"file_type": "xlsx", "percentage": 12.82},
    {"file_type": "png",  "percentage": 10.26},
    {"file_type": "jpg",  "percentage": 19.23},
    {"file_type": "zip",  "percentage": 7.69},
    {"file_type": "txt",  "percentage": 15.38}
]

        }
        return Response(data)
    

class OverallAnalyticsAPIView(APIView):
    def get(self, request, format=None):
        data = {
            "file_list": 100,
            "documents": 40,
            "tag_relation": 80,
            "worflow": 5,
            "document_type": 2,
            "tag_type": 8,
        }
        return Response(data)
 