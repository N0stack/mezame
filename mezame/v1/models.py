import uuid

from django.db import models


class Image(models.Model):
    IMAGE_FORMAT_CHOICES = (
        ('iso', 'ISO'),
        ('qcow2', 'qcow2'),
    )

    IMAGE_STATUS_INACTIVE = 0
    IMAGE_STATUS_ACTIVE = 1
    IMAGE_STATUS_DEACTIVATED = 2
    IMAGE_STATUS_CHOICES = (
        (IMAGE_STATUS_INACTIVE, 'inactive'),
        (IMAGE_STATUS_ACTIVE, 'active'),
        (IMAGE_STATUS_DEACTIVATED, 'deactivated'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    status = models.TextField(choices=IMAGE_STATUS_CHOICES, default=IMAGE_STATUS_INACTIVE)
    disk_format = models.TextField(choices=IMAGE_FORMAT_CHOICES, null=True)
    size_byte = models.BigIntegerField(default=0)
    virtual_size_byte = models.BigIntegerField(default=0)
    min_disk_byte = models.BigIntegerField(default=0)
    min_ram_byte = models.BigIntegerField(default=0)
    checksum = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True)
    deleted = models.BooleanField(default=False)
