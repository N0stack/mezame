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
    size_byte = models.BigIntegerField(default=0) # Unimplemented
    virtual_size_byte = models.BigIntegerField(default=0) # Unimplemented
    min_disk_byte = models.BigIntegerField(default=0) # Unimplemented
    min_ram_byte = models.BigIntegerField(default=0) # Unimplemented
    checksum = models.TextField(blank=True) # Unimplemented
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None, null=True) # Unimplemented
    deleted = models.BooleanField(default=False) # Unimplemented


class Agent(models.Model):
    AGENT_STATUS_INACTIVE = 0
    AGENT_STATUS_ACTIVE = 1
    AGENT_STATUS_ERROR = 1
    AGENT_STATUS_CHOICES = (
        (AGENT_STATUS_INACTIVE, 'inactive'),
        (AGENT_STATUS_ACTIVE, 'active'),
        (AGENT_STATUS_ERROR, 'error'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(default='')
    status = models.TextField(choices=AGENT_STATUS_CHOICES, default=AGENT_STATUS_INACTIVE)
    host = models.TextField(default='')
    images = models.ManyToManyField(Image)
