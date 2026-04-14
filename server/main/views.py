import os

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.files.uploadedfile import InMemoryUploadedFile
from time import sleep


class StatusView(APIView):
    """ Возвращает статус сервера 200"""

    def get(self, request):
        return Response(status=status.HTTP_200_OK)


class ControlView(APIView):
    """ Управление сервером """

    def get(self, request):
        password = "123456"
        command = f"echo {password} | sudo -S /usr/sbin/shutdown now"
        os.system(f'echo "{password}" | sudo -S systemctl stop runner')
        sleep(1)
        os.system(command)
        return Response(status=status.HTTP_200_OK)
