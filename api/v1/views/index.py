#!/usr/bin/python3
# api/v1/views/index.py

from flask import jsonify
from api.v1.views import app_views


# Create a route /status on the app_views object
@app_views.route('/api/v1/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})
