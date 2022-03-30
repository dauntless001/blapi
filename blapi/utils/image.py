from datetime import datetime

def image_path(instance, filename):
    path = datetime.today().date()
    return f'{instance._meta.model_name}/{path}/{filename}'