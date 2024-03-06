#app/url.py
from django.urls import path 
from .views import index
from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    path('', index, name = 'index'),
    path('list/', RecipeListView.as_view(), name = "recipe-list" ),
    path('detail/<int:pk>/', RecipeDetailView.as_view(), name="recipe-detail")
]

app_name = "ledger"
