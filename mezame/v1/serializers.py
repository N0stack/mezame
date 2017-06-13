from rest_framework import serializers

from .models import Image
from .models import Agent


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
        read_only_fields = ('id',)


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = (
            'id',
            'name',
            'status',
            'host',
            'images',
        )
        read_only_fields = ('id',)
        depth = 1

