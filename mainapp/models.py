from django.db import models, connection
from django.contrib.auth.models import User

def create_dynamic_table(table_name, fields):

    class Meta:
        db_table = table_name

    # Prepare fields for the dynamic model
    attributes = {
        '__module__': __name__,  # Required to associate the model with the current module
        'Meta': Meta,           # Attach metadata to the model
    }
    attributes.update(fields)  # Add fields to the dynamic model

    # Create the dynamic model class
    DynamicModel = type(table_name.capitalize(), (models.Model,), attributes)

    # Use the schema editor to create the table in the database
    with connection.schema_editor() as schema_editor:
        schema_editor.create_model(DynamicModel)

    return DynamicModel  # Return the created model
