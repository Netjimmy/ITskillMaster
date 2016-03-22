# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models



# class Jobstored(models.Model):
    # jobno = models.AutoField(primary_key=True)
    # srcno = models.CharField(max_length=30, blank=True, null=True)
    # postdate = models.DateField(blank=True, null=True)
    # title = models.CharField(max_length=150, blank=True, null=True)
    # company = models.CharField(max_length=150, blank=True, null=True)
    # industry = models.CharField(max_length=50, blank=True, null=True)
    # locno = models.CharField(max_length=150, blank=True, null=True)
    # emptypeno = models.CharField(max_length=50, blank=True, null=True)
    # exp = models.CharField(max_length=100, blank=True, null=True)
    # salary = models.CharField(max_length=100, blank=True, null=True)
    # content = models.TextField(blank=True, null=True)
    # url = models.CharField(max_length=150, blank=True, null=True)
	
    # def __unicode__(self):
       # return self.title

    # class Meta:
        # managed = False
        # db_table = 'jobstored'


class Job(models.Model):
    jobno = models.AutoField(primary_key=True)
    src = models.CharField(max_length=50, blank=True, null=True)
    postdate = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    company = models.CharField(max_length=150, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    loc = models.CharField(max_length=50, blank=True, null=True)
    emptype = models.CharField(max_length=50, blank=True, null=True)
    exp = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    skill = models.TextField(blank=True, null=True)  # This field type is a guess.
    url = models.CharField(unique=True, max_length=120)
    cluster = models.SmallIntegerField(blank=True, null=True)
	
    def __unicode__(self):
       return self.title

    class Meta:
        managed = False
        db_table = 'job'
        ordering = ['-postdate']

class Location(models.Model):
    no = models.IntegerField(primary_key=True)
    loc = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'location'
