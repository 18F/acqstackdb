from django.contrib import admin

# Register your models here.
from .models import Acquisition, Agency, Subagency, ContractingOffice, ContractingOfficer, COR, Evaluator, Release

@admin.register(Acquisition, Agency, Subagency, ContractingOffice, ContractingOfficer, COR, Evaluator, Release)
class AcquisitionAdmin(admin.ModelAdmin):
    pass
