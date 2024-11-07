from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path("logout/", views.logout_view, name="logout"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('expenditure-form/', views.expenditure_form, name='expenditure_form'),
    path('income-form/', views.income_form, name='income_form'),
    path('index/', views.index, name='index'),
    path('add-expenditure/', views.add_expenditure, name='add_expenditure'),
    path('add-income/', views.add_income, name='add_income'),
    path('income-list/', views.income_list, name='income_list'),
    path('expenditure-list/', views.expenditure_list, name='expenditure_list'),
    path('sales-form/', views.sales_form, name='sales_form'),
    path('add-sales/', views.add_sales, name='add_sales'),
    path('sales-list/', views.sales_list, name='sales_list'),
    path('purchases-form/', views.purchases_form, name='purchases_form'),
    path('add-purchases/', views.add_purchases, name='add_purchases'),
    path('purchases-list/', views.purchases_list, name='purchases_list'),
    path('delete-income/<int:income_id>/', views.delete_income, name='delete-income'),
    path('delete-purchase/<int:purchase_id>/', views.delete_purchase, name='delete-purchase'),
    path('delete-sale/<int:sale_id>/', views.delete_sale, name='delete-sale'),
    path('delete-expenditure/<int:expenditure_id>/', views.delete_expenditure, name='delete-expenditure'),
    path('update-income/<int:income_id>/', views.update_income, name='update-income'),
    path('update-expenditure/<int:expenditure_id>/', views.update_expenditure, name='update-expenditure'),
    path('update-sale/<int:sale_id>/', views.update_sale, name='update-sale'),
    path('update-purchase/<int:purchase_id>/', views.update_purchase, name='update-purchase'),
]


