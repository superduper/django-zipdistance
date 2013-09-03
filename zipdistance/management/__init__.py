from django.db.models.signals import post_migrate, post_syncdb
from django.core.management import call_command
import django
import zipdistance.models

def load_zip_codes(sender, **kwargs):
    if sender.ZipDistance.objects.all().count():
        print "Skipping: zipdistance fixture load"
    else:
        print "Executing: zipdistance fixture load"
        call_command('loaddata', 'zipcodes')


a, b, c, d, f = django.VERSION
if a == 1 and b >= 7:
    post_migrate.connect(load_zip_codes, sender=zipdistance.models)
else:
    post_syncdb.connect(load_zip_codes, sender=zipdistance.models)
