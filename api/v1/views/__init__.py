# api/v1/views/__init__.py

from flask import Blueprint

# Create a Blueprint instance with the url prefix /api/v1
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import the views from the package
from api.v1.views.index import *
