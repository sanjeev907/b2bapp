from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from accounts.models.users import User
from accounts.models.profile import *
from accounts.models.family import *
from accounts.models.bankaccount import *
from accounts.models.address import *
# Register your models here.

class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['mobile_number']

class HobbyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name',]

class InterestAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name',]

class UserTypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name',]

class UserprofileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display =['user',] 

class CompanyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'company_type', 'firm_image', 'pan_number', 'gst_in', 'gst_image', 'user', 'is_active']

class SpouseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name',]

class ParentsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['name',]

class KidsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['name',]

class BankAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name',]

class IfscAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name',]

class BankAccountAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['account_holder_name','account_number','confirm_account_number','ifsc','account_type']

class ZoneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name',] 

class CountryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name',]

class StateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name','country','zone',]

class CityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name',]

class PincodeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name',]


admin.site.register(Zone, ZoneAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Pincode, PincodeAdmin)
admin.site.register(Address)
admin.site.register(User, UserAdmin)
admin.site.register(Hobby, HobbyAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(UserType, UserTypeAdmin)
admin.site.register(UserProfile, UserprofileAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Spouse,SpouseAdmin)
admin.site.register(Parents,ParentsAdmin)
admin.site.register(Kids,KidsAdmin)
admin.site.register(Bank,BankAdmin)
admin.site.register(Ifsc,IfscAdmin)
admin.site.register(BankAccount,BankAccountAdmin)