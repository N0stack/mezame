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

    def create(self, validated_data: dict):
        return Image.objects.create(**validated_data)

    def update(self, instance: Image, validated_data: dict):
        instance.name = validated_data.get('name', instance.name)
        instance.status = validated_data.get('status', instance.status)
        instance.disk_format = validated_data.get('disk_format', instance.disk_format)
        instance.size_byte = validated_data.get('size_byte', instance.size_byte)
        instance.virtual_size_byte = validated_data.get('virtual_size_byte', instance)
        instance.min_disk_byte = validated_data.get('min_disk_byte', instance)
        instance.min_ram_byte = validated_data.get('min_ram_byte', instance)
        instance.checksum = validated_data.get('checksum', instance)
        instance.deleted_at = validated_data.get('deleted_at', instance)
        instance.deleted = validated_data.get('deleted', instance)
        return instance
