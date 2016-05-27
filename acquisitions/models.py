from django.db import models

# Create your models here.
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
    subagency=models.ForeignKey(Subagency)
    contracting_officer=models.ForeignKey(ContractingOfficer)
    contracting_officer_representative=models.ForeignKey(COR)
    contracting_office=models.ForeignKey(ContractingOffice)
    product_owner=models.CharField(max_length=50)
    task=models.CharField(max_length=100, blank=False)
    rfq_id=models.IntegerField()
    period_of_performance=models.DateField()
    dollars=models.IntegerField()
    set_aside_status=models.CharField(options=SET_ASIDE_CHOICES)
    amount_of_competition=models.IntegerField()
    contract_type=models.CharField(options=CONTRACT_TYPE_CHOICES)
    description=models.TextField(max_length=500)
    naics=models.IntegerField(max_length=6)
    competition_strategy=models.CharField(options=COMPETITION_STRATEGY_CHOICES)
    procurement_method=models.CharField(options=PROCUREMENT_METHOD_CHOICES)
    award_date=models.DateField()
    delivery_date=models.DateField()

    def __str__(self):
        return "%s (%s - %s)" % self.task, self.agency, self.subagency

    class Meta:
        ordering = ('rfq_id',)

class Agency(models.Model):
    name=models.CharField()

    def __str__(self):
        return self.name

class Subagency(models.Model):
    name=models.CharField()
    agency=models.ForeignKey(Agency)

    def __str__(self):
        return "%s - %s" % self.name, self.agency

    class Meta:
        ordering = ('name',)

class ContractingOffice(models.Model):
    name=models.CharField()

    def __str__(self):
        return self.name

class ContractingOfficer(models.Model):
    name=models.CharField()
    contracting_office=models.ForeignKey(ContractingOffice)

    def __str__(self):
        return "%s - %s" % self.name, self.contracting_office

    class Meta:
        ordering = ('name',)

class COR(models.Model):
    name=models.CharField()

    def __str__(self):
        return self.name

class Evaluator(models.Model):
    name=models.CharField()
    acquisition=models.ManyToManyField(Acquisition)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Releases(models.Model):
    acquisition=models.ForeignKey(Acquisition)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ('id')
