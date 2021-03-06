# Generated by Django 2.0 on 2017-12-16 00:49

from django.db import migrations

def data_migration(apps, schema_editor):
#{
    Color = apps.get_model('hfapp', 'Color')
    
    Color(id='1R', name='red').save()
    Color(id='2G', name='green').save()
    Color(id='3B', name='blue').save()
    Color(id='4_', name='colorless').save()
    
    WeaponGroup = apps.get_model('hfapp', 'WeaponGroup')
    
    WeaponGroup(id='Sw', name='Sword').save()
    WeaponGroup(id='La', name='Lance').save()
    WeaponGroup(id='Ax', name='Axe').save()
    WeaponGroup(id='Bw', name='Bow').save()
    WeaponGroup(id='Dg', name='Dagger').save()
    WeaponGroup(id='Tm', name='Tome').save()
    WeaponGroup(id='St', name='Staff').save()
    WeaponGroup(id='Br', name='Breath').save()
#}

class Migration(migrations.Migration):

    dependencies = [
        ('hfapp', '0003_auto_20171215_1647'),
    ]

    operations = [
        migrations.RunPython(data_migration)
    ]
