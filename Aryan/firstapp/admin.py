from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Database)
class DataAdmin(admin.ModelAdmin):
    pass
@admin.register(countries)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(companyinfo)
class PurchaseAdmin(admin.ModelAdmin):
    pass

@admin.register(gemtype)
class gemtype(admin.ModelAdmin):
    pass 
@admin.register(POJ)
class PurchaseOFJewell(admin.ModelAdmin):
    pass

@admin.register(Currency)
class Curr(admin.ModelAdmin):
    pass

@admin.register(centerstone)
class cstone(admin.ModelAdmin):
    pass


@admin.register(loc)
class locationdf(admin.ModelAdmin):
    pass
@admin.register(certificate)
class cert(admin.ModelAdmin):
    pass

@admin.register(colorofcstone)
class COCSadmin(admin.ModelAdmin):
    pass
@admin.register(metal1)
class metaladmin(admin.ModelAdmin):
    pass
@admin.register(jewell)
class jewelladmin(admin.ModelAdmin):
    pass
@admin.register(shape1)
class ShapePOJ(admin.ModelAdmin):
    pass


