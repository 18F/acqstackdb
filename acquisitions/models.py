from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Agency(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subagency(models.Model):
    name=models.CharField(max_length=100)
    agency=models.ForeignKey(Agency)

    def __str__(self):
        return "%s - %s" % (self.name, self.agency)

    class Meta:
        ordering = ('name',)

class ContractingOffice(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ContractingOfficer(models.Model):
    name=models.CharField(max_length=100)
    contracting_office=models.ForeignKey(ContractingOffice)

    def __str__(self):
        return "%s - %s" % (self.name, self.contracting_office)

    class Meta:
        ordering = ('name',)

class COR(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

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
    # TODO: add set-asides here
    )

    CONTRACT_TYPE_CHOICES=(
    # TODO: add contract types here
    )

    COMPETITION_STRATEGY_CHOICES=(
    # TODO: add competition strategies here
    )

    PROCUREMENT_METHOD_CHOICES=(
    # TODO: add procurement methods here
    )

    AWARD_STATUS_CHOICES=(
        (1,"18F - Qual"),
        (2,"OGC - Qual"),
        (3,"OGP - Qual"),
        (4,"18F - Agreement Scoping"),
        (5,"18F - Agreement Approval"),
        (6,"OGC - Agreement Approval"),
        (7,"18F - RFQ Scoping"),
        (8,"OGC - RFQ Scoping"),
        (9,"OGP - RFQ Scoping"),
        (10," 18F - RFQ Ready"),
        (11," 18F - RFQ on Street"),
        (12," 18F - Eval"),
        (13," OGC - Eval"),
        (14," OGP - Eval"),
        (15," 18F - Award"),
        (16," OGC - Award"),
        (17," OGP - Award"),
        (18," 18F - Post-award"),
    )

    agency=models.ForeignKey(Agency, blank=False)
    subagency=models.ForeignKey(Subagency)
    contracting_officer=models.ForeignKey(ContractingOfficer, null=True, blank=True)
    contracting_officer_representative=models.ForeignKey(COR, null=True, blank=True)
    contracting_office=models.ForeignKey(ContractingOffice, null=True, blank=True)
    vendor=models.ForeignKey(Vendor, null=True, blank=True)
    award_status=models.IntegerField(default=0,blank=False,
                                choices=AWARD_STATUS_CHOICES)
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
