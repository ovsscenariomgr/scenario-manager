import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return super(OverwriteStorage, self).get_available_name(name, max_length)

def scenario_upload_to(scenario_id, sub_dir, filename):
    return os.path.join('%s' % scenario_id, sub_dir, filename)

def media_upload_to(instance, filename):
    return scenario_upload_to(instance.scenario_id, 'media', filename)

def vocals_upload_to(instance, filename):
    return scenario_upload_to(instance.scenario_id, 'vocals', filename)

def image_upload_to(instance, filename):
    return scenario_upload_to(instance.profile.scenario_id, 'images', filename)
