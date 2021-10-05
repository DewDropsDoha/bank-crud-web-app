from django.urls import path 

from .views import (
    home_view,
    deposit_view,
    withdraw_view,
    transaction_view,
)

app_name = 'bank' #used fo html linking(href)
urlpatterns = [
    path('', home_view, name='home'),
    path('deposit/', deposit_view, name='deposit'),
    path('withdraw/', withdraw_view, name='withdraw'),
    path('transaction/', transaction_view, name='transaction'),
]
