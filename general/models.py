from django.db import models
from django.db.models.fields.files import ImageField


class MaintenanceEquipment(models.Model):

    WINDOW = 'Window'
    TOLIET = 'Toilet'
    BED = 'Bed'
    CABINET = 'Cabinet'
    TABLE = 'Table'
    CHAIR = 'Chair'

    CATEGORY_CHOICES = [
        (WINDOW, 'Window'),
        (TOLIET, 'Toilet'),
        (BED, 'Bed'),
        (CABINET, 'Cabinet'),
        (TABLE, 'Table'),
        (CHAIR, 'Chair'),
    ]

    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    image_Url = models.CharField(max_length=2083)


class MaintenanceRequest(models.Model):

    COMPLETED = 'Completed'
    UNCOMPLETE = 'Uncomplete'

    PROGRESS_CHOICES = [
        (COMPLETED, 'Completed'),
        (UNCOMPLETE, 'Uncomplete'),
    ]

    WINDOW = 'Window'
    TOLIET = 'Toilet'
    BED = 'Bed'
    CABINET = 'Cabinet'
    TABLE = 'Table'
    CHAIR = 'Chair'

    CATEGORY_CHOICES = [
        (WINDOW, 'Window'),
        (TOLIET, 'Toilet'),
        (BED, 'Bed'),
        (CABINET, 'Cabinet'),
        (TABLE, 'Table'),
        (CHAIR, 'Chair'),
    ]

    category = models.CharField(
        max_length=255, choices=CATEGORY_CHOICES)
    progress = models.CharField(
        max_length=255, choices=PROGRESS_CHOICES)
    # created = models.DateTimeField(default=False)
    remark = models.CharField(max_length=255)
    hostel = models.CharField(max_length=255)


class RecordEquipment(models.Model):
    category = models.CharField(max_length=255)
    created = models.DateTimeField()
    remark = models.CharField(max_length=255)
