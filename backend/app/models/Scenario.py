import os
import shutil
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.db.models import Model

class Scenario(Model):
    # header = OneToOneField(Header)
    # profile = OneToOneField(Profile)
    # vocalfiles = ForeignKey(VocalFile)
    # mediafiles = ForeignKey(MediaFile)
    # init = OneToOneField(ScenarioInit)
    # eventgroups = ForeignKey(EventGroup) -- This will be rendered as 'events' per XML spec
    # scenes = ForeignKey(Scene) -- Will be 'flattened' in rendered XML
    pass

# Make all necessary directories for this scenario    
@receiver(post_save, sender=Scenario)
def create_file_dir(sender, instance, **kwargs):
    os.makedirs(os.path.join(settings.MEDIA_ROOT, str(instance.pk), 'images'), exist_ok=True)
    os.makedirs(os.path.join(settings.MEDIA_ROOT, str(instance.pk), 'media'), exist_ok=True)
    os.makedirs(os.path.join(settings.MEDIA_ROOT, str(instance.pk), 'vocals'), exist_ok=True)

# Cleanup files for scenario on delete
@receiver(post_delete, sender=Scenario)
def remove_file_dir(sender, instance, **kwargs):
    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, str(instance.pk)))