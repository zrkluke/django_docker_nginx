from django.db import migrations
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password
from accounts.models import CustomUser


def initEmployee(apps, schema_editor):
    employee_user = CustomUser.objects.create(username='employee_user', password=make_password('initium'))
    employee_group = Group.objects.get(name='accounts_employee')
    employee_user.groups.add(employee_group)
    employee_user.save()


def deleteEmployee(apps, schema_editor):
    employee_user = CustomUser.objects.get(username='employee_user')
    employee_group = Group.objects.get(name='accounts_employee')
    employee_user.groups.remove(employee_group)
    employee_user.save()
    CustomUser.objects.filter(username='employee_user').delete()



class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initGroup'),
    ]

    operations = [
                migrations.RunPython(initEmployee, deleteEmployee),
    ]
