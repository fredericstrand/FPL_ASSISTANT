from django.shortcuts import render

def index(request):
    return redner(request, 'frontend/build/index.html')

from rest_framework.response import Response
from rest_framework.decorators import api_view
import joblib  # Assuming you're using joblib to load the ML model

# Load your pre-trained machine learning model
model = joblib.load('path/to/your_model.pkl')

@api_view(['GET'])
def get_recommendations(request):
    # Sample logic to generate recommendations
    player_data = request.query_params.get('data', None)  # Example data from React frontend
    # You would normally process this data with your ML model
    if player_data:
        recommendations = model.predict([player_data])
        return Response({"recommendations": recommendations})
    return Response({"error": "No player data provided"}, status=400)
