from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin, OrderedTabularInline

# Register your models here.
from .models import Acquisition, Agency, Subagency, ContractingOffice, \
                    ContractingOfficer, COR, Evaluator, Release, Vendor, \
                    Role, Step, Track, Stage, StageTrackThroughModel


@admin.register(Agency, Subagency, ContractingOffice, ContractingOfficer, COR,
                Evaluator, Release, Vendor, Role, Track)
class AdminAdmin(admin.ModelAdmin):
    pass


class AcquisitionAdmin(admin.ModelAdmin):
    filter_horizontal = ('roles',)


class StageTrackThroughModelInline(OrderedTabularInline):
    model = StageTrackThroughModel
    fields = ('track', 'order', 'move_up_down_links',)
    readonly_fields = ('order', 'move_up_down_links',)
    extra = 1
    ordering = ('order',)


class StageAdmin(OrderedModelAdmin):
    list_display = ('name',)
    inlines = (StageTrackThroughModelInline,)

    def get_urls(self):
        urls = super(StageAdmin, self).get_urls()
        for inline in self.inlines:
            if hasattr(inline, 'get_urls'):
                urls = inline.get_urls(self) + urls
        return urls


class StepAdmin(OrderedModelAdmin):
    list_display = ('actor', 'move_up_down_links')

admin.site.register(Acquisition, AcquisitionAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(Step, StepAdmin)
