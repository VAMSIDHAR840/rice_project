from django.urls import path, include
from backend.views import *

urlpatterns = [
    path('dashboard', Dashboard.as_view(), name="dashboard"),
    path('add_category', AddCategory.as_view(), name="add_category"),
    path('view_category', ViewCategory.as_view(), name="view_category"),
    path('edit_category', EditCategory.as_view(), name="edit_category"),
    path('delete_category', DeleteCategory.as_view(), name="delete_category"),
    path('add_brand',  AddBrand.as_view(), name="add_brand"),
    path('edit_brand',  EditBrand.as_view(), name="edit_brand"),
    path('delete_brand',  DeleteBrand.as_view(), name="delete_brand"),
    path('add_user',  AddUser.as_view(), name="add_user"),
    path('edit_user',  EditUser.as_view(), name="edit_user"),
    path('delete_user',  DeleteUser.as_view(), name="delete_user"),
    path('payment_add',  PaymentAdd.as_view(), name="payment_add"),
    path('payment_edit',  PaymentEdit.as_view(), name="payment_edit"),
    path('remainder_add',  RemainderAdd.as_view(), name="remainder_add"),
    path('remainder_edit',  RemainderEdit.as_view(), name="remainder_edit"),
    path('remainder_delete',  RemainderDelete.as_view(), name="remainder_delete"),
    path('add_purchase',  PurchaseAdd.as_view(), name="add_purchase"),
    path('edit_purchase',  PurchaseEdit.as_view(), name="edit_purchase"),
    path('delete_purchase',  PurchaseDelete.as_view(), name="delete_purchase"),
    path('tracing_add',  TracindAdd.as_view(), name="tracing_add"),
    path('tracing_edit',  TracindEdit.as_view(), name="tracing_edit"),
    path('tracing_delete',  TracindDelete.as_view(), name="tracing_delete"),
    path('remainder_add',  RemainderAdd.as_view(), name="remainder_add"),
    path('remainder_edit',  RemainderEdit.as_view(), name="remainder_edit"),
    path('remainder_delete',  RemainderDelete.as_view(), name="remainder_delete"),
    path('add_order',  AddOrder.as_view(), name="add_order"),
    path('edit_order',  EditOrder.as_view(), name="edit_order"),
    path('delete_order',  DeleteOrder.as_view(), name="delete_order"),
]

