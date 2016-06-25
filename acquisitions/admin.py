from django.contrib import admin

# Register your models here.
from .models import Acquisition, Agency, Subagency, ContractingOffice, \
                    ContractingOfficer, COR, Evaluator, Release, Vendor, \
                    Role, AwardStatus, Track


@admin.register(Agency, Subagency, ContractingOffice, ContractingOfficer, COR,
                Evaluator, Release, Vendor, Role, AwardStatus, Track)
class AdminAdmin(admin.ModelAdmin):
    pass


class AcquisitionAdmin(admin.ModelAdmin):
    filter_horizontal = ('roles',)

admin.site.register(Acquisition, AcquisitionAdmin)
