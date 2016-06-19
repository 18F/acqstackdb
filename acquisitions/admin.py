from django.contrib import admin

# Register your models here.
from .models import Acquisition, Agency, Subagency, ContractingOffice, ContractingOfficer, COR, Evaluator, Release, Vendor, AwardStatus

@admin.register(Acquisition, Agency, Subagency, ContractingOffice, ContractingOfficer, COR, Evaluator, Release, Vendor, AwardStatus)
class AcquisitionAdmin(admin.ModelAdmin):
    pass
