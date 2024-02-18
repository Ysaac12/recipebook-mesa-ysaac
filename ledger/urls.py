from django.urls import path 
from .views import index
from .views import recipes_list
from .views import recipes_list_1
from .views import recipes_list_2

urlpatterns = [
    path('', index, name = 'index'),
    path('list', recipes_list, name = 'recipes-list' ),
    path('1', recipes_list_1, name = 'rescipes-list-1' ),
    path('2', recipes_list_2, name = 'recipes-list-2')
]

app_name = "ledger"
