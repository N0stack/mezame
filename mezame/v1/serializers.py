from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'id',
            'name',
            'status',
            'disk_format',
            'size_byte',
            'virtual_size_byte',
            'min_disk_byte',
            'min_ram_byte',
            'checksum',
            'created_at',
            'updated_at',
            'deleted_at',
            'deleted',
        )
