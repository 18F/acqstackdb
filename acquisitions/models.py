from django.db import models

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

    agency=models.ForeignKey(Agency, blank=False)
    subagency=models.ForeignKey(Subagency, null=True)
    contracting_officer=models.ForeignKey(ContractingOfficer, null=True)
    contracting_officer_representative=models.ForeignKey(COR, null=True)
    contracting_office=models.ForeignKey(ContractingOffice, null=True)
    product_owner=models.CharField(max_length=50, null=True)
    task=models.CharField(max_length=100, blank=False)
    rfq_id=models.IntegerField(null=True)
    period_of_performance=models.DateField(null=True)
    dollars=models.IntegerField(null=True)
    set_aside_status=models.CharField(max_length=100, choices=SET_ASIDE_CHOICES, null=True)
    amount_of_competition=models.IntegerField(null=True)
    contract_type=models.CharField(max_length=100, choices=CONTRACT_TYPE_CHOICES, null=True)
    description=models.TextField(max_length=500, null=True)
    naics=models.IntegerField(null=True)
    competition_strategy=models.CharField(max_length=100,
                                        choices=COMPETITION_STRATEGY_CHOICES, null=True)
    procurement_method=models.CharField(max_length=100,
                                        choices=PROCUREMENT_METHOD_CHOICES, null=True)
    award_date=models.DateField(null=True)
    delivery_date=models.DateField(null=True)

    def __str__(self):
        return "%s (%s - %s)" % (self.task, self.agency, self.subagency)

    class Meta:
        ordering = ('rfq_id',)

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
