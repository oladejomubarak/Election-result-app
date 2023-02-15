from django.db import models


# Create your models here.

class AgentName(models.Model):
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=255, null=False)
    polling_unit = models.ForeignKey("PollingUnit", on_delete=models.PROTECT)


class AnnouncedLgaResults(models.Model):
    lga_name = models.CharField(max_length=255)
    party_abbreviation = models.CharField(max_length=4)
    party_source = models.IntegerField()
    entered_by_user = models.CharField(max_length=255)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=255)


class AnnouncedPuResults(models.Model):
    polling_unit = models.ForeignKey('PollingUnit', on_delete=models.PROTECT)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=255)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=255)


class AnnouncedStateResults(models.Model):
    state_name = models.CharField(max_length=255)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=255)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=255)


class AnnouncedWardResults(models.Model):
    ward_name = models.CharField(max_length=255)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=255)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=255)


class Lga(models.Model):
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=255)
    state = models.ForeignKey('State', on_delete=models.PROTECT)
    lga_description = models.TextField()
    entered_by_user = models.CharField(max_length=255)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=255)


class Party(models.Model):
    party_id = models.IntegerField()
    party_name = models.CharField(max_length=11)


class PollingUnit(models.Model):
    polling_unit_id = models.IntegerField()
    ward = models.ForeignKey('Ward', on_delete=models.PROTECT)
    lga_id = models.IntegerField()
    polling_unit_number = models.CharField(max_length=50)
    polling_unit_name = models.CharField(max_length=50)
    polling_unit_description = models.TextField()
    lat = models.CharField(max_length=255)
    long = models.CharField(max_length=255)
    entered_by_user = models.CharField(max_length=255)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=255)


class State(models.Model):
    state_name = models.CharField(max_length=50)


class Ward(models.Model):
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga = models.ForeignKey(Lga, on_delete=models.PROTECT)
    ward_description = models.TextField()
    entered_by_user = models.CharField(max_length=255)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=255)
