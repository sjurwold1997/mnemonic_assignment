from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_accounts, name='overview'),
    path('<int:account_id>/', views.select_account, name='select'),
    path('destination/', views.prepare_transfer, name='prepare-transfer'),
    path('transfer/', views.transfer_money, name='execute-transfer'),
    path('all-tranfsers/', views.see_all_transfers, name='transfers')
]