from os import path
import shutil

from django.conf import settings
from django.http import Http404
# from django.core.files.uploadedfile import UploadedFile
from django.http.response import FileResponse
from rest_framework import viewsets
from rest_framework import exceptions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.views import Request
from rest_framework.views import Response
from rest_framework.parsers import FileUploadParser

from .models import Image
from .serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_fields = ('status', 'disk_format')


class ImageFile(APIView):
    parser_classes = (FileUploadParser,)

    def get_object(self, image_id: str):
        try:
            return Image.objects.get(id=image_id)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request: Request, image_id: str, format=None):

        # is_image_record_exists
        if not Image.objects.filter(id=image_id).exists():
            raise exceptions.NotFound

        # is_image_binary_exists
        if not path.exists(path.join(settings.MEZAME_PATH, image_id)):
            return Response(status=status.HTTP_204_NO_CONTENT)

        return FileResponse(open(path.join(settings.MEZAME_PATH, image_id), 'rb'))

    def put(self, request: Request, image_id: str, format=None):
        image = self.get_object(image_id)

        if image.status == str(Image.IMAGE_STATUS_ACTIVE):
            return Response(status=status.HTTP_409_CONFLICT)

        if image.status == str(Image.IMAGE_STATUS_DEACTIVATED):
            return Response(status=status.HTTP_403_FORBIDDEN)

        if image.status == str(Image.IMAGE_STATUS_INACTIVE):

            # ToDo: PUTされたファイルの拡張子を確認し、disk_formatを変更
            # ToDo: POST /image 時に指定されたフォーマット以外を弾く
            # if image.disk_format is not None && [disk_formatと違っていたらFalse]:
            #     return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)

            # file_obj: UploadedFile
            file_obj = request.data['file']

            with open(path.join(settings.MEZAME_PATH, image_id), 'wb+') as f:
                if file_obj.multiple_chunks():
                    for chunk in file_obj.chunks():
                        f.write(chunk)
                else:
                    f.write(file_obj.read())

            image.status = Image.IMAGE_STATUS_ACTIVE
            image.save()

            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ImagePath(APIView):
    def get_object(self, image_id: str):
        try:
            return Image.objects.get(id=image_id)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request: Request, image_id: str, format=None):
        image = self.get_object(image_id)

        if image.status == str(Image.IMAGE_STATUS_ACTIVE):
            data = {'path': path.join(settings.MEZAME_PATH, image_id)}
            return Response(data=data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request: Request, image_id: str, format=None):
        src_path = request.data.get('src_path', None)

        if src_path is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        image = self.get_object(image_id)

        if image.status == str(Image.IMAGE_STATUS_ACTIVE):
            return Response(status=status.HTTP_409_CONFLICT)

        if image.status == str(Image.IMAGE_STATUS_DEACTIVATED):
            return Response(status=status.HTTP_403_FORBIDDEN)

        if image.status == str(Image.IMAGE_STATUS_INACTIVE):
            # ToDo: directory traversal 対策
            shutil.copy(
                path.join(settings.MEZAME_CONF['SHARED_DIR_PATH'], src_path),
                path.join(settings.MEZAME_PATH, image_id)
            )

            image.status = Image.IMAGE_STATUS_ACTIVE
            image.save()

            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
