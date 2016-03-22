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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Cluster(models.Model):
    cid = models.IntegerField(db_column='cID', primary_key=True)  # Field name made lowercase.
    clustervector = models.TextField(db_column='clusterVector', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'cluster'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    url = models.CharField(unique=True, max_length=200)
    cluster = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job'


class Jobstorage(models.Model):
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
    url = models.CharField(max_length=200, blank=True, null=True)
    cluster = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobstorage'


class Jobstored(models.Model):
    jobno = models.AutoField(primary_key=True)
    srcno = models.CharField(max_length=30, blank=True, null=True)
    postdate = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    company = models.CharField(max_length=150, blank=True, null=True)
    industry = models.CharField(max_length=50, blank=True, null=True)
    locno = models.CharField(max_length=150, blank=True, null=True)
    emptypeno = models.CharField(max_length=50, blank=True, null=True)
    exp = models.CharField(max_length=100, blank=True, null=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobstored'


class Location(models.Model):
    no = models.IntegerField(primary_key=True)
    loc = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'location'


class Test(models.Model):
    jobno = models.AutoField(primary_key=True)
    srcno = models.CharField(max_length=30, blank=True, null=True)
    postdate = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    company = models.CharField(max_length=150, blank=True, null=True)
    industry = models.CharField(max_length=50, blank=True, null=True)
    locno = models.CharField(max_length=150, blank=True, null=True)
    emptypeno = models.CharField(max_length=50, blank=True, null=True)
    exp = models.CharField(max_length=100, blank=True, null=True)
    salary = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'
