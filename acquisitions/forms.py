import floppyforms.__future__ as forms
from .models import Acquisition

class ExtraSelectInput(forms.Select):
    template_name = './floppyforms/extra-select.html'

class AcquisitionForm(forms.ModelForm):
    class Meta:
        model = Acquisition
        fields = ['agency','subagency','contracting_officer','contracting_officer_representative','contracting_office','vendor','award_status','product_owner','task','rfq_id','period_of_performance','dollars','set_aside_status','amount_of_competition','contract_type','description','naics','competition_strategy','procurement_method','award_date','delivery_date']
        widgets = {
         'contracting_officer_representative': ExtraSelectInput()
         }
