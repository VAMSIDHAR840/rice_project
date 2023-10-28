from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class login(TemplateView):
    template_name = "login.html"
    context = None

class Dashboard(TemplateView):
    template_name = 'backend/dashboard.html'
    context = None

class AddCategory(TemplateView):
    template_name = 'backend/add_category.html'
    context = None

class ViewCategory(TemplateView):
    template_name = 'backend/category.html'
    context = None

class EditCategory(TemplateView):
    template_name = 'backend/edit_category.html'
    context = None
class DeleteCategory(TemplateView):
    template_name = 'backend/delete_category.html'
    context = None

class AddBrand(TemplateView):
    template_name = 'backend/add_brand.html'
    context = None

class EditBrand(TemplateView):
    template_name = 'backend/edit_brand.html'
    context = None

class DeleteBrand(TemplateView):
    template_name = 'backend/delete_brand.html'
    context = None

class AddUser(TemplateView):
    template_name = 'backend/add_user.html'
    context = None

class EditUser(TemplateView):
    template_name = 'backend/edit_user.html'
    context = None

class DeleteUser(TemplateView):
    template_name = 'backend/delete_user.html'
    context = None

class PaymentAdd(TemplateView):
    template_name = 'backend/payment_add.html'
    context = None

class PaymentEdit(TemplateView):
    template_name = 'backend/payment_edit.html'
    context = None        

class RemainderAdd(TemplateView):
    template_name = 'backend/remainder_add.html'
    context = None   

class RemainderEdit(TemplateView):
    template_name = 'backend/remainder_edit.html'
    context = None  

class RemainderDelete(TemplateView):
    template_name = 'backend/remainder_delete.html'
    context = None      

class PurchaseAdd(TemplateView):
    template_name = 'backend/add_purchase.html'
    context = None      

class PurchaseEdit(TemplateView):
    template_name = 'backend/edit_purchase.html'
    context = None      

class PurchaseDelete(TemplateView):
    template_name = 'backend/delete_purchase.html'
    context = None     

class TracindAdd(TemplateView):
    template_name = 'backend/tracing_add.html'
    context = None      

class TracindEdit(TemplateView):
    template_name = 'backend/tracing_edit.html'
    context = None      

class TracindDelete(TemplateView):
    template_name = 'backend/tracing_delete.html'
    context = None      

class RemainderAdd(TemplateView):
    template_name = 'backend/remainder_add.html'
    context = None     


class RemainderEdit(TemplateView):
    template_name = 'backend/remainder_edit.html'
    context = None 

class RemainderDelte(TemplateView):
    template_name = 'backend/remainder_delete.html'
    context = None 

class AddOrder(TemplateView):
    template_name = 'backend/add_order.html'
    context = None     

class EditOrder(TemplateView):
    template_name = 'backend/edit_order.html'
    context = None 

class DeleteOrder(TemplateView):
    template_name = 'backend/delete_order.html'
    context = None 