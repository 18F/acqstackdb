from django.db import models
from django.core.validators import RegexValidator
from django.db.models import F

# Create your models here.
class Agency(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Agencies"

class Subagency(models.Model):
    name=models.CharField(max_length=100)
    agency=models.ForeignKey(Agency)

    def __str__(self):
        return "%s - %s" % (self.name, self.agency)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Subagencies"

class ContractingOffice(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contracting Office"
        verbose_name_plural = "Contracting Offices"

class ContractingOfficer(models.Model):
    name=models.CharField(max_length=100)
    contracting_office=models.ForeignKey(ContractingOffice)

    def __str__(self):
        return "%s - %s" % (self.name, self.contracting_office)

    class Meta:
        ordering = ('name',)
        verbose_name = "Contracting Officer"
        verbose_name_plural = "Contracting Officers"

class COR(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Contracting Officer Representative"
        verbose_name_plural = "Contracting Officer Representatives"

# Is the acquisition internal or external?
class Track(models.Model):
    name = models.CharField(max_length=30, default="External")

    def __str__(self):
        return "%s" % (self.name)

class AwardStatus(models.Model):

    status = models.CharField(max_length=50)
    actor = models.CharField(max_length=50)
    track = models.ForeignKey(Track, blank=False)
    ordering = models.IntegerField(editable=False)
    is_before = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return "%s - %s" % (self.status, self.actor,)

    def natural_key(self):
        return (self.status, self.actor,)

    def save(self):
        # stvnrlly: I'm not sure if this should be in save() or pre_save() or whatever,
        # but I'm not sure that it matters since it'll run for all objects either way
        if not self.pk: # Only run if this entry didn't exist previously
            statuses_length = len(AwardStatus.objects.all())
            if statuses_length > 0 and self.is_before_id:
                try:
                    # Find object currently pointing to is_before
                    current_before = AwardStatus.objects.get(track=self.track, is_before_id=self.is_before_id)
                    # Borrow the is_before from that object
                    self.is_before_id = current_before.is_before_id
                    self.ordering = current_before.ordering + 1
                    # Update object to point to new status
                    current_before.is_before_id = self.id
                    current_before.save()
                except self.DoesNotExist:
                    # This is the new first award status in the process
                    self.ordering = 0
                # Find the object that this status is_before
                next_status = AwardStatus.objects.get(track=self.track, id=self.is_before_id)
                # Find all objects with that order or higher and increment all filtered objects by 1
                higher_statuses = AwardStatus.objects.filter(ordering__gte=next_status.ordering).update(ordering=F('ordering') + 1)
            elif statuses_length > 0:
                # This is the last award status in the process
                # TODO: should be one more than the highest order
                # TODO: make previous last status point to this one
                pass
            else:
                # This is the first entry
                self.ordering=0
                self.is_before=None
        super(AwardStatus, self).save()

    class Meta:
        # ordering = ['-status', 'actor']
        verbose_name_plural = "Award Statuses"


class Vendor(models.Model):
    name=models.CharField(max_length=200, blank=False)
    email=models.EmailField(blank=False)
    duns=models.CharField(max_length=9, blank=False, validators=[
        RegexValidator(regex='^\d{9}$',message="DUNS number must be 9 digits")
    ])

    def __str__(self):
        return self.name

class Acquisition(models.Model):
    SET_ASIDE_CHOICES=(
        ("AbilityOne", "AbilityOne"),
        ("HUBZone Small Business", "HUBZone Small Business"),
        ("Multiple Small Business Categories",
            "Multiple Small Business Categories"),
        ("Other Than Small", "Other Than Small"),
        ("Service Disabled Veteran-owned Small Business",
            "Service Disabled Veteran-owned Small Business"),
        ("Small Business", "Small Business"),
        ("Small Disadvantaged Business (includes Section 8a)",
            "Small Disadvantaged Business (includes Section 8a)"),
        ("To Be Determined-BPA", "To Be Determined-BPA"),
        ("To Be Determined-IDIQ", "To Be Determined-IDIQ"),
        ("Veteran-Owned Small Business", "Veteran-Owned Small Business"),
        ("Woman-Owned Small Business", "Woman-Owned Small Business"),
    )

    CONTRACT_TYPE_CHOICES=(
        ("Cost No Fee", "Cost No Fee"),
        ("Cost Plus Award Fee", "Cost Plus Award Fee"),
        ("Cost Plus Fixed Fee", "Cost Plus Fixed Fee"),
        ("Cost Plus Incentive Fee", "Cost Plus Incentive Fee"),
        ("Cost Sharing", "Cost Sharing"),
        ("Fixed Price","Fixed Price"),
        ("Fixed Price Award Fee", "Fixed Price Award Fee"),
        ("Fixed Price Incentive", "Fixed Price Incentive"),
        ("Fixed Price Labor Hours","Fixed Price Labor Hours"),
        ("Fixed Price Level of Effort","Fixed Price Level of Effort"),
        ("Fixed Price Time and Materials","Fixed Price Time and Materials"),
        ("Fixed Price with Economic Price Adjustment",
            "Fixed Price with Economic Price Adjustment"),
        ("Interagency Agreement", "Interagency Agreement"),
        ("Labor Hours", "Labor Hours"),
        ("Labor Hours and Time and Materials","Labor Hours and Time and Materials"),
        ("Order Dependent", "Order Dependent"),
        ("Time and Materials", "Time and Materials"),
    )

    COMPETITION_STRATEGY_CHOICES=(
        ("Sole Source", "Sole Source"),
        ("Full and Open", "Full and Open"),
        ("Set-Aside", "Set-Aside"),
        ("Partial Small Business Set-Aside",
            "Partial Small Business Set-Aside"),
        ("A/E Procedures", "A/E Procedures"),
        ("Full and Open Competition", "Full and Open Competition"),
        ("Not Available for Competition (e.g., 8a sole source, HUBZone & \
            SDVOSB sole source, Ability One, all > SAT)",
            "Not Available for Competition (e.g., 8a sole source, HUBZone & \
            SDVOSB sole source, Ability One, all > SAT)"),
        ("Not Competed (e.g., sole source, urgency, etc., all > SAT)",
            "Not Competed (e.g., sole source, urgency, etc., all > SAT)"),
        ("Full and Open after exclusion of sources (competitive small \
            business set-asides, competitive 8a)",
            "Full and Open after exclusion of sources (competitive small \
            business set-asides, competitive 8a)"),
        ("Follow On to Competed Action", "Follow On to Competed Action"),
        ("Competed under SAP", "Competed under SAP"),
        ("Not Competed under SAP (e.g., Urgent, Sole source, Logical \
            Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)",
            "Not Competed under SAP (e.g., Urgent, Sole source, Logical \
            Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)"),
        ("Competitive Delivery Order Fair Opportunity Provided",
            "Competitive Delivery Order Fair Opportunity Provided"),
        ("Non-Competitive Delivery Order", "Non-Competitive Delivery Order"),
        ("Fair Opportunity", "Fair Opportunity"),
        ("Sole-Source", "Sole-Source"),
        ("Limited Sources", "Limited Sources"),
        ("Competitive Schedule Buy", "Competitive Schedule Buy"),
        ("Full and Open after exclusion of sources (competitive small business \
            set-asides, competitive 8a)",
            "Full and Open after exclusion of sources (competitive small \
            business set-asides, competitive 8a)"),
        ("Full and Open Competition Unrestricted",
            "Full and Open Competition Unrestricted"),
        ("Not Available for Competition (e.g., 8a sole source, HUBZone & \
            SDVOSB sole source, Ability One, all > SAT)",
            "Not Available for Competition (e.g., 8a sole source, HUBZone & \
            SDVOSB sole source, Ability One, all > SAT)"),
        ("Not Competed (e.g., sole source, urgency, etc., all > SAT)",
            "Not Competed (e.g., sole source, urgency, etc., all > SAT)"),
        ("Not Competed under SAP (e.g., Urgent, Sole source, Logical \
            Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)",
            "Not Competed under SAP (e.g., Urgent, Sole source, Logical \
            Follow-On, 8a, HUBZone & SDVOSB sole source, all < SAT)"),
        ("A/E Procedures", "A/E Procedures"),
        ("Competed under SAP", "Competed under SAP"),
        ("Follow On to Competed Action (FAR 6.302-1)",
            "Follow On to Competed Action (FAR 6.302-1)"),
        ("Limited Sources FSS Order", "Limited Sources FSS Order"),
        ("Competitive Schedule Buy", "Competitive Schedule Buy"),
        ("Partial Small Business Set-Aside",
            "Partial Small Business Set-Aside"),
    )

    PROCUREMENT_METHOD_CHOICES=(
        ("GSA Schedule", "GSA Schedule"),
        ("Government-wide Agency Contract-GWAC",
            "Government-wide Agency Contract-GWAC"),
        ("Basic Ordering Agreement", "Basic Ordering Agreement"),
        ("Blanket Purchase Agreement-BPA", "Blanket Purchase Agreement-BPA"),
        ("Multi-Agency Contract", "Multi-Agency Contract"),
        ("BPA Call", "BPA Call"),
        ("Purchase Order", "Purchase Order"),
        ("Definitive Contract", "Definitive Contract"),
        ("Ability One", "Ability One"),
        ("Indefinite Delivery Indefinite Quantity-IDIQ",
            "Indefinite Delivery Indefinite Quantity-IDIQ"),
        ("Negotiated", "Negotiated"),
        ("Sealed Bid", "Sealed Bid"),
        ("Contract", "Contract"),
        ("Commercial Item Contract", "Commercial Item Contract"),
        ("GSA Schedules Program BPA", "GSA Schedules Program BPA"),
        ("Indefinite Delivery Vehicle (IDV)",
            "Indefinite Delivery Vehicle (IDV)"),
        ("Purchase Order", "Purchase Order"),
        ("Order under IDV", "Order under IDV"),
        ("Order under GSA Schedules Program",
            "Order under GSA Schedules Program"),
        ("Order under GSA Schedules Program BPA",
            "Order under GSA Schedules Program BPA"),
        ("Definitive Contract other than IDV",
            "Definitive Contract other than IDV"),
        ("Indefinite Delivery Vehicle Base Contract",
            "Indefinite Delivery Vehicle Base Contract"),
        ("Order under GSA Federal Supply Schedules Program",
            "Order under GSA Federal Supply Schedules Program"),
        ("Order under IDV", "Order under IDV"),
        ("Purchase Order", "Purchase Order"),
        ("Contract modification", "Contract modification"),
        ("Ability One", "Ability One"),
        ("Call Order under GSA Schedules BPA",
            "Call Order under GSA Schedules BPA"),
        ("GSA Schedule Contract", "GSA Schedule Contract"),
        ("Negotiated", "Negotiated"),
        ("Sealed Bid", "Sealed Bid"),
        ("Government-wide Agency Contract-GWAC",
            "Government-wide Agency Contract-GWAC"),
        ("Commercial Item Contract", "Commercial Item Contract"),
        ("GSA Schedules Program BPA", "GSA Schedules Program BPA"),
        ("Basic Ordering Agreement", "Basic Ordering Agreement"),
        ("Blanket Purchase Agreement-BPA", "Blanket Purchase Agreement-BPA"),
        ("Multi-Agency Contract", "Multi-Agency Contract"),
    )

    agency=models.ForeignKey(Agency, blank=False)
    subagency=models.ForeignKey(Subagency)
    contracting_officer=models.ForeignKey(ContractingOfficer, null=True, blank=True)
    contracting_officer_representative=models.ForeignKey(COR, null=True, blank=True)
    contracting_office=models.ForeignKey(ContractingOffice, null=True, blank=True)
    vendor=models.ForeignKey(Vendor, null=True, blank=True)
    award_status=models.ForeignKey(AwardStatus, default=0, blank=False)
    track=models.ForeignKey(Track, blank=False)
    product_owner=models.CharField(max_length=50, null=True, blank=True)
    task=models.CharField(max_length=100, blank=False)
    rfq_id=models.IntegerField(null=True, blank=True)
    period_of_performance=models.DateField(null=True, blank=True)
    dollars=models.DecimalField(decimal_places=2, max_digits=14, null=True, blank=True)
    set_aside_status=models.CharField(max_length=100, choices=SET_ASIDE_CHOICES, null=True, blank=True)
    amount_of_competition=models.IntegerField(null=True, blank=True)
    contract_type=models.CharField(max_length=100, choices=CONTRACT_TYPE_CHOICES, null=True, blank=True)
    description=models.TextField(max_length=500, null=True, blank=True)
    naics=models.IntegerField(null=True, blank=True)
    competition_strategy=models.CharField(max_length=100,
                                        choices=COMPETITION_STRATEGY_CHOICES, null=True, blank=True)
    procurement_method=models.CharField(max_length=100,
                                        choices=PROCUREMENT_METHOD_CHOICES, null=True, blank=True)
    award_date=models.DateField(null=True, blank=True)
    delivery_date=models.DateField(null=True, blank=True)

    def __str__(self):
        return "%s (%s)" % (self.task, self.subagency)

class Evaluator(models.Model):
    name=models.CharField(max_length=100)
    acquisition=models.ManyToManyField(Acquisition)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Release(models.Model):
    acquisition=models.ForeignKey(Acquisition)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ('id',)
