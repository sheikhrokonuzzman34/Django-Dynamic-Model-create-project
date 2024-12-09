from django.shortcuts import render, redirect
from django.apps import apps
from django.http import JsonResponse
from .dynamic_model_creator import create_dynamic_table
from django.contrib.auth.decorators import login_required
from django.db import models

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
