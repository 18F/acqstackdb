from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin, OrderedTabularInline

# Register your models here.
from .models import Acquisition, Agency, Subagency, ContractingOffice, \
                    ContractingOfficer, COR, Evaluator, Release, Vendor, \
                    Role, Actor, Step, Track, Stage, StepTrackThroughModel


@admin.register(Agency, Subagency, ContractingOffice, ContractingOfficer, COR,
                Evaluator, Release, Vendor, Role, Actor, Track)
class AdminAdmin(admin.ModelAdmin):
    pass


class AcquisitionAdmin(admin.ModelAdmin):
    filter_horizontal = ('roles',)


class StepTrackThroughModelInline(OrderedTabularInline):
    model = StepTrackThroughModel
    fields = ('track', 'order', 'move_up_down_links',)
    readonly_fields = ('order', 'move_up_down_links',)
    extra = 1
    ordering = ('order',)


class StepAdmin(OrderedModelAdmin):
    list_display = ('actor', 'stage',)
    inlines = (StepTrackThroughModelInline,)

    def get_urls(self):
        urls = super(StepAdmin, self).get_urls()
        for inline in self.inlines:
            if hasattr(inline, 'get_urls'):
                urls = inline.get_urls(self) + urls
        return urls


class StageAdmin(OrderedModelAdmin):
    list_display = ('name', 'move_up_down_links')

admin.site.register(Stage, StageAdmin)
admin.site.register(Acquisition, AcquisitionAdmin)
admin.site.register(Step, StepAdmin)
