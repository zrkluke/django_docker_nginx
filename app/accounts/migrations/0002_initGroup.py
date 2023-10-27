from django.db import migrations
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group, Permission


def initGroup(apps, schema_editor):
    # initial "Employee" group
    employee, created = Group.objects.get_or_create(name='accounts_employee')


def deleteGroup(apps, schema_editor):
    group_name = 'accounts_employee'
    Group.objects.filter(name=group_name).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
                migrations.RunPython(initGroup, deleteGroup),
    ]
