from django.contrib import admin
from testapp.models import Expenses

# Register your models here.

class ExpensesAdmin(admin.ModelAdmin):
    list_display=['itemno' , 'itemname', 'amount', 'paidby', 'purchasedate', 'remarks']

# class LoginAdmin(admin.ModelAdmin):
#     list_display=['username','password']

admin.site.register(Expenses,ExpensesAdmin)

# admin.site.register(Login,LoginAdmin)

