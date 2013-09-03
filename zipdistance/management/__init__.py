from django.db.models.signals import post_syncdb
from django.core.management import call_command

import zipdistance.models

def load_zip_codes(sender, **kwargs):
    if sender.ZipDistance.objects.all().count():
        pass
    else:
        call_command('loaddata', 'zipcodes')
    
post_migrate.connect(load_zip_codes, sender=zipdistance.models)