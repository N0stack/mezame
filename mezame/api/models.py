import uuid

from django.db import models


class Image(models.Model):
    IMAGE_FORMAT_CHOICES = (
        ('iso', 'ISO'),
        ('qcow2', 'qcow2'),
    )

    STATUS_INACTIVE = 0
    STATUS_ACTIVE = 1
    STATUS_DEACTIVATED = 2
    STATUS_CHOICES = (
        (STATUS_INACTIVE, 'inactive'),
        (STATUS_ACTIVE, 'active'),
        (STATUS_DEACTIVATED, 'deactivated'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    status = models.TextField(choices=STATUS_CHOICES, default=STATUS_INACTIVE)
    disk_format = models.TextField(choices=IMAGE_FORMAT_CHOICES, null=True)
    size_byte = models.BigIntegerField(default=0) # Unimplemented
    virtual_size_byte = models.BigIntegerField(default=0) # Unimplemented
    min_disk_byte = models.BigIntegerField(default=0) # Unimplemented
    min_ram_byte = models.BigIntegerField(default=0) # Unimplemented
    checksum = models.TextField(blank=True) # Unimplemented
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(default=None, null=True) # Unimplemented
    deleted = models.BooleanField(default=False) # Unimplemented
